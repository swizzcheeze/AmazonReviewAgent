"""Agent pipeline orchestrating writer and editor steps."""
from dataclasses import dataclass
from typing import Protocol


class Provider(Protocol):
    def generate(self, prompt: str) -> str:
        ...


@dataclass
class Agent:
    provider: Provider

    def run(self, prompt: str) -> str:
        return self.provider.generate(prompt)


@dataclass
class ReviewPipeline:
    writer: Agent
    editor: Agent

    def run(self, notes: str, context: str = "") -> str:
        prompt = f"Write a product review. Notes: {notes}\n{context}".strip()
        draft = self.writer.run(prompt)
        edit_prompt = (
            "Improve, humanize, and polish the following product review.\n"
            f"{draft}"
        )
        final = self.editor.run(edit_prompt)
        return final
