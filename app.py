"""
The Loom - Web Interface
Transparent window into the query → bake → study → sing → response pipeline
"""

import gradio as gr
from bridge import LoomBridge

loom = LoomBridge()

def process_query(query: str, api_key: str = "") -> str:
    """
    Process a query through The Loom's three sacred katas
    
    Args:
        query: User's question or contemplation
        api_key: Optional OpenAI API key for Swamiji wisdom
        
    Returns:
        Full pipeline visualization showing the spiritual journey
    """
    if not query or query.strip() == "":
        return "Please enter a query for The Loom to contemplate."
    
    if not loom.health_check():
        return "The Loom core is not accessible. Please ensure the Lisp executable is compiled."
    
    response = loom.query(query.strip(), api_key=api_key.strip() if api_key else None)
    return response

def create_interface():
    """Create the Gradio web interface"""
    
    custom_css = """
    .gradio-container {
        background: linear-gradient(135deg, #F5F3F0 0%, #E6D5E8 30%, #AED9E0 70%, #F5F3F0 100%) !important;
    }
    .gradio-container, .gradio-container * {
        color: #6B4E71 !important;
    }
    .prose, .prose *, p, span, div {
        color: #6B4E71 !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #6B4E71 !important;
        font-weight: 600 !important;
    }
    strong, b {
        color: #C8A2C8 !important;
    }
    em, i {
        color: #6B4E71 !important;
        font-style: italic !important;
    }
    .block {
        background-color: rgba(230, 213, 232, 0.4) !important;
        border: 1px solid rgba(200, 162, 200, 0.3) !important;
        border-radius: 12px !important;
    }
    label {
        color: #6B4E71 !important;
        font-weight: 500 !important;
    }
    textarea, input {
        background-color: rgba(255, 255, 255, 0.7) !important;
        border: 1px solid rgba(200, 162, 200, 0.4) !important;
        color: #6B4E71 !important;
    }
    button {
        background: linear-gradient(135deg, #B8C5B2 0%, #AED9E0 100%) !important;
        border: none !important;
        color: #6B4E71 !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 8px rgba(184, 197, 178, 0.3) !important;
    }
    button:hover {
        background: linear-gradient(135deg, #AED9E0 0%, #C8A2C8 100%) !important;
        box-shadow: 0 4px 12px rgba(174, 217, 224, 0.4) !important;
    }
    .markdown {
        color: #6B4E71 !important;
    }
    """
    
    with gr.Blocks(
        title="The Loom - Constitutional AI",
        css=custom_css
    ) as app:
        
        gr.Markdown("""
        # The Loom - Constitutional AI
        
        **Constitutional AI grounded in nondual reality, the Dao, and Advaita Vedanta**
        """)
        
        with gr.Row():
            with gr.Column(scale=2):
                query_input = gr.Textbox(
                    label="Your Query",
                    placeholder="Enter your question or contemplation...",
                    lines=3,
                    max_lines=5
                )
                
                api_key_input = gr.Textbox(
                    label="OpenAI API Key (Optional)",
                    placeholder="sk-... (for Swamiji Wisdom enhancement)",
                    type="password",
                    lines=1
                )
                
                submit_btn = gr.Button("Connect", variant="primary", size="lg")
                
                gr.Markdown("""
                The Loom processes your queries through transformative stages:
                
                1. **Bake** - Turn raw data into holistic truth models
                2. **Study** - Apply laws of nature, observe, and analyze results
                3. **Sing** - Make complex insights engaging, understandable, and useful
                4. **Swamiji Wisdom** - OpenAI enhances with compassionate clarity (if API key provided)
                
                *Grounded in: Nonduality, Common Good, Consequences, Humility*
                """)
        
        with gr.Row():
            with gr.Column(scale=3):
                response_output = gr.Textbox(
                    label="",
                    lines=25,
                    max_lines=30,
                    show_copy_button=True
                )
        
        submit_btn.click(
            fn=process_query,
            inputs=[query_input, api_key_input],
            outputs=[response_output]
        )
        
        query_input.submit(
            fn=process_query,
            inputs=[query_input, api_key_input],
            outputs=[response_output]
        )
        
        gr.Markdown("""
        ---
        *The Loom: Engine in Common Lisp | Interface in Python/Gradio | Constitution: Sacred ethics*
        
        **Om tat sat om**
        """)
    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch(
        server_name="0.0.0.0",
        server_port=5000,
        show_error=True
    )
