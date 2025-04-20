import gradio as gr
from main import get_recommend_courses


with gr.Blocks() as demo:
    
    gr.Markdown("<h1 style='text-align: center;'>Analytics Vidhya Course Recommender</h1>")
    # Assign a custom CSS ID for styling
    with gr.Column(elem_id="a4-container"):  
        txt = gr.Textbox(label="Prompt")
        
        txt_3 = gr.Textbox(value="", label="Output")
        
        btn = gr.Button(value="Submit")
        btn.click(get_recommend_courses, inputs=[txt], outputs=[txt_3])
       
    # Custom CSS for A4 width
    demo.css = """
    #a4-container {
        max-width: 793px;  /* Approximate A4 width in pixels */
        margin: 0 auto;    /* Center align */
    }
    """

demo.launch()
