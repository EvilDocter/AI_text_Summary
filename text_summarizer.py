import streamlit as st
from llm import ask_ai

# Set page configuration for a balanced side-by-side layout
st.set_page_config(
    page_title="AI-Powered Text Summarizer",
    page_icon="📝",
    layout="wide",
)

# Clean, minimalistic styling with cool summarizing animation
st.markdown(
    """
<style>
    /* Overall layout spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1250px;
    }

    /* Column headers */
    .column-header {
        font-size: 1.15rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    /* Idle placeholder state */
    .placeholder-card {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 320px;
        border: 2px dashed rgba(128, 128, 128, 0.25);
        border-radius: 12px;
        background: rgba(128, 128, 128, 0.02);
        color: rgba(128, 128, 128, 0.7);
        text-align: center;
        padding: 2rem;
    }
    .placeholder-icon {
        font-size: 2.2rem;
        margin-bottom: 0.5rem;
    }

    /* Cool Summarizing Animation (Pulsing AI Orb + Glowing Shimmer Lines) */
    .processing-card {
        min-height: 320px;
        border: 1px solid rgba(99, 102, 241, 0.35);
        border-radius: 12px;
        padding: 1.8rem;
        background: rgba(99, 102, 241, 0.03);
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .processing-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-weight: 600;
        color: #6366f1;
        margin-bottom: 1.6rem;
        font-size: 1.05rem;
    }
    .ai-orb {
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: #6366f1;
        box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.7);
        animation: orb-pulse 1.4s cubic-bezier(0.2, 0.6, 0.4, 1) infinite;
    }
    @keyframes orb-pulse {
        0% {
            box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.7);
        }
        70% {
            box-shadow: 0 0 0 14px rgba(99, 102, 241, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(99, 102, 241, 0);
        }
    }
    .shimmer-line {
        height: 12px;
        margin-bottom: 1.1rem;
        border-radius: 6px;
        background: linear-gradient(90deg, rgba(128, 128, 128, 0.12) 25%, rgba(128, 128, 128, 0.28) 50%, rgba(128, 128, 128, 0.12) 75%);
        background-size: 200% 100%;
        animation: shimmer-sweep 1.6s infinite;
    }
    .w-95 { width: 95%; }
    .w-80 { width: 80%; }
    .w-88 { width: 88%; }
    .w-65 { width: 65%; }
    @keyframes shimmer-sweep {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }

    /* Result summary card */
    .summary-card {
        min-height: 320px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 12px;
        padding: 1.6rem;
        background: rgba(128, 128, 128, 0.04);
        line-height: 1.7;
        font-size: 1.05rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# App Title & Description
st.title("AI-Powered Text Summarizer")
st.caption(
    "Paste your text on the left and generate a clean, concise summary on the right."
)
st.write("")

# Side-by-side columns: Input on the left, Summary on the right
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.markdown('<div class="column-header">Source Text</div>', unsafe_allow_html=True)
    text_input = st.text_area(
        "Enter text to summarize:",
        placeholder="Paste your paragraph or article here...",
        height=300,
        label_visibility="collapsed",
    )
    summarize_clicked = st.button("Summarize", type="primary", use_container_width=True)

with col_right:
    st.markdown('<div class="column-header">Summary</div>', unsafe_allow_html=True)
    result_area = st.empty()

    # Default idle state before user clicks Summarize
    result_area.markdown(
        """
        <div class="placeholder-card">
            <div class="placeholder-icon">📋</div>
            <p style="margin: 0; font-size: 1rem; font-weight: 500;">Ready to summarize</p>
            <p style="margin: 0.3rem 0 0 0; font-size: 0.85rem;">Paste text on the left and click <strong>Summarize</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Process summarization when button is clicked
if summarize_clicked:
    # Step 1: Input validation (empty or whitespace check)
    if text_input.strip() == "":
        col_left.warning("Please enter some text before summarizing.")
    else:
        # Step 2: Show cool summarizing animation in the right column
        result_area.markdown(
            """
            <div class="processing-card">
                <div class="processing-header">
                    <div class="ai-orb"></div>
                    <span>AI is reading and condensing your text...</span>
                </div>
                <div class="shimmer-line w-95"></div>
                <div class="shimmer-line w-80"></div>
                <div class="shimmer-line w-88"></div>
                <div class="shimmer-line w-65"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Step 3: Construct prompt for Gemini
        prompt = f"""Please provide a clear and concise summary of the following text.
Follow these guidelines:
- Summarize the text in clear, simple language.
- Preserve the main ideas and important facts.
- Remove unnecessary repetition and irrelevant details.
- Avoid introducing information that is not present in the original text.
- Produce a shorter version of the input.
- Use bullet points only when they improve readability.

TEXT:
{text_input}"""

        # Step 4: Request summary via ask_ai()
        try:
            summary = ask_ai(prompt)
            if summary and summary.strip():
                # Display final summary cleanly in the right column
                with result_area.container():
                    st.markdown(
                        f"""
                        <div class="summary-card">
                        {summary}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            else:
                result_area.error("No summary could be generated. Please try again.")
        except Exception as e:
            result_area.error(f"Failed to generate summary: {e}")
