"""Command-line interface for the AI-Powered Review Assistant."""
import datetime
import os
from typing import Optional

from config import load_config, save_config
from fetcher import fetch_product_context
from pipeline import Agent, ReviewPipeline
from providers import get_provider


def slugify(name: str) -> str:
    return "".join(c if c.isalnum() else "_" for c in name).strip("_").lower()


def build_pipeline(cfg: dict) -> ReviewPipeline:
    writer_name = cfg["pipeline"]["writer_provider"]
    editor_name = cfg["pipeline"]["editor_provider"]
    writer = Agent(get_provider(writer_name, cfg["providers"][writer_name]))
    editor = Agent(get_provider(editor_name, cfg["providers"][editor_name]))
    return ReviewPipeline(writer, editor)


def ensure_reviews_dir() -> None:
    os.makedirs("reviews", exist_ok=True)


def write_review(with_context: bool = False) -> None:
    cfg = load_config()
    product = input("Product name: ").strip()
    rating = input("Rating (1-5): ").strip()
    notes = input("Notes: ").strip()

    context = ""
    if with_context:
        url = input("Product URL: ").strip()
        if url:
            context = fetch_product_context(url)

    pipeline = build_pipeline(cfg)
    review_text = pipeline.run(notes, context)

    ensure_reviews_dir()
    filename = (
        datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        + "_"
        + slugify(product)
        + ".txt"
    )
    with open(os.path.join("reviews", filename), "w", encoding="utf-8") as f:
        f.write(f"Product: {product}\nRating: {rating}\n\n{review_text}\n")
    print(f"Review saved to reviews/{filename}")


def list_reviews() -> None:
    ensure_reviews_dir()
    files = sorted(os.listdir("reviews"))
    if not files:
        print("No reviews found.")
        return
    for f in files:
        print(f)


def settings_menu() -> None:
    cfg = load_config()
    print("Current writer provider:", cfg["pipeline"]["writer_provider"])
    new_writer = input(
        "Enter writer provider (gemini/ollama/lmstudio/openrouter) or blank to keep: "
    ).strip().lower()
    if new_writer:
        cfg["pipeline"]["writer_provider"] = new_writer
    print("Current editor provider:", cfg["pipeline"]["editor_provider"])
    new_editor = input(
        "Enter editor provider (gemini/ollama/lmstudio/openrouter) or blank to keep: "
    ).strip().lower()
    if new_editor:
        cfg["pipeline"]["editor_provider"] = new_editor
    if "gemini" in {cfg["pipeline"]["writer_provider"], cfg["pipeline"]["editor_provider"]}:
        key = input("Enter Gemini API key (blank to keep current): ").strip()
        if key:
            cfg["providers"]["gemini"]["api_key"] = key
    if "openrouter" in {cfg["pipeline"]["writer_provider"], cfg["pipeline"]["editor_provider"]}:
        key = input("Enter OpenRouter API key (blank to keep current): ").strip()
        if key:
            cfg["providers"]["openrouter"]["api_key"] = key
        model = input("Enter OpenRouter model (blank to keep current): ").strip()
        if model:
            cfg["providers"]["openrouter"]["model"] = model
    save_config(cfg)
    print("Configuration saved.")


def main() -> None:
    while True:
        print("\nAI Review Assistant")
        print("1. Write a new review")
        print("2. Write a new review with product context")
        print("3. List past reviews")
        print("4. Settings")
        print("5. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            write_review(False)
        elif choice == "2":
            write_review(True)
        elif choice == "3":
            list_reviews()
        elif choice == "4":
            settings_menu()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
