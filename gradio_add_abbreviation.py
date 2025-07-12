import gradio as gr
from textcleaner_partha.add_abbreviation import add_abbreviation
import os

# Optional: Create abbreviation_mappings folder if not exist
os.makedirs("abbreviation_mappings", exist_ok=True)


def handle_abbreviation_addition(file_name, abbreviation, full_form):
    if not file_name.endswith(".json"):
        file_name += ".json"

    try:
        add_abbreviation(file_name, abbreviation, full_form)
        return f"✅ Abbreviation '{abbreviation}' added to '{file_name}' as: {full_form}"
    except Exception as e:
        return f"❌ Failed to add abbreviation: {e}"


with gr.Blocks(title="Abbreviation Mapping Tool") as app:
    gr.Markdown("## 📚 Add Abbreviation to Mapping File")

    with gr.Row():
        file_input = gr.Textbox(label="Mapping File (e.g., slang.json or common)", placeholder="slang or common")
        abbr_input = gr.Textbox(label="Abbreviation (e.g., idk)")
        full_form_input = gr.Textbox(label="Full Form (e.g., I don't know)")

    submit_btn = gr.Button("Add Abbreviation")
    output_box = gr.Textbox(label="Status", show_copy_button=True)

    submit_btn.click(
        fn=handle_abbreviation_addition,
        inputs=[file_input, abbr_input, full_form_input],
        outputs=output_box
    )

app.launch()