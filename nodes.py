class PromptSE:
    """
    A simple node for creating, editing, and combining custom prompt entries.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "user_input": ("STRING", {"multiline": True, "default": ""}),
            },
            "hidden": {
                "promptse_data": ("STRING", {"multiline": True, "default": "{}"}),
            },
        }

    CATEGORY = "PromptSE"
    FUNCTION = "process"
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("output_string", "llm_input",)

    def __init__(self):
        # Default data structure
        self.default_data = {
            "entries": [
                {
                    "id": "entry_ltx23_default",
                    "title": "LTX2.3 Structured Prompt",
                    "content": "风格 / 画幅\n镜头角度 + 运镜\n角色：年龄、外貌、穿着\n场景：地点、时间、光线\n具体动作\n具体物理声音\n对话",
                    "enabled": True,
                    "weight": 1.0
                }
            ],
            "settings": {
                "connector": ", ",
                "mode": "M",
                "weightFormat": "parentheses",
                "modelTemplate": "ltx23",
                "language": "zh",
                "llmModel": {
                    "name": "gpt-4o-mini",
                    "task": "video_prompt_generation"
                }
            },
            "lexicon": []
        }

    def process(self, promptse_data="{}", user_input="", **kwargs):
        """
        Process the prompt data and return the combined string.
        """
        import json

        print(f"PromptSE: Received raw data: '{promptse_data}'")

        # Parse the data from the widget
        try:
            if isinstance(promptse_data, str) and promptse_data.strip():
                data = json.loads(promptse_data)
                print(f"PromptSE: Parsed data successfully: {data}")
            else:
                data = self.default_data
                print(f"PromptSE: Using default data: {data}")
        except (json.JSONDecodeError, Exception) as e:
            print(f"PromptSE: Error parsing data: {e}, using default")
            data = self.default_data

        settings = data.get("settings", {})
        mode = settings.get("mode", "M")
        connector = settings.get("connector", ", ")
        weight_format = settings.get("weightFormat", "parentheses")
        language = settings.get("language", "zh")
        llm_model_cfg = settings.get("llmModel", "gpt-4o-mini")
        llm_model = llm_model_cfg.get("name", "gpt-4o-mini") if isinstance(llm_model_cfg, dict) else str(llm_model_cfg or "gpt-4o-mini")
        entries = data.get("entries", [])

        print(f"PromptSE: Processing - Mode: {mode}, Connector: '{connector}', Weight Format: {weight_format}, Entries: {len(entries)}")

        def format_content_with_weight(content, weight):
            """Format content with weight according to the specified format"""
            if weight_format == "none" or weight == 1.0:
                return content
            elif weight_format == "parentheses":
                return f"({content}:{weight:.1f})"
            elif weight_format == "brackets":
                return f"[{content}:{weight:.1f}]"
            else:
                return content

        final_parts = []

        if mode == "S":
            # Single mode: find the first enabled entry
            for entry in entries:
                if entry.get("enabled", False):
                    content = entry.get("content", "").strip()
                    weight = entry.get("weight", 1.0)
                    if content:
                        formatted_content = format_content_with_weight(content, weight)
                        final_parts.append(formatted_content)
                        print(f"PromptSE: Single mode - selected: '{formatted_content}' (weight: {weight})")
                    break
        else:
            # Multiple mode: concatenate all enabled entries
            for entry in entries:
                if entry.get("enabled", False):
                    content = entry.get("content", "").strip()
                    weight = entry.get("weight", 1.0)
                    if content:
                        formatted_content = format_content_with_weight(content, weight)
                        final_parts.append(formatted_content)
                        print(f"PromptSE: Multiple mode - added: '{formatted_content}' (weight: {weight})")

        output_string = connector.join(final_parts)

        normalized_user_input = (user_input or "").strip()
        selected_terms = ", ".join(final_parts)
        if selected_terms:
            llm_input = (
                f"Model={llm_model}; Task=video_prompt_generation; Language={language}. "
                f"Combine ALL selected terms into one coherent video generation prompt. "
                f"Preserve key visual, motion, lighting, audio, and negative constraints. "
                f"Selected terms: {selected_terms}. "
                f"User language input: {normalized_user_input if normalized_user_input else 'None'}. "
                "Output only the final polished prompt text."
            )
        else:
            llm_input = ""

        print(f"PromptSE: Generated output: '{output_string}'")
        print(f"PromptSE: LLM input: '{llm_input}'")
        return (output_string, llm_input)

# Test the node
if __name__ == "__main__":
    node = PromptSE()
    print("Input types:", node.INPUT_TYPES())
    print("Test output:", node.process())
