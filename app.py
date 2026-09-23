import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import gradio as gr
from rock_mass_rating_rmr_calculator import compute_rmr

def rmr_interface(ucs, rqd, spacing, joint_condition, groundwater):
    try:
        if None in (ucs, rqd, spacing, joint_condition, groundwater):
            return "# **Error:** All inputs must be filled.", None
        ucs = float(ucs)
        rqd = float(rqd)
        spacing = float(spacing)
        # Clamp to allowed ranges
        ucs = max(0.1, min(400, ucs))
        rqd = max(0, min(100, rqd))
        spacing = max(0.001, min(10, spacing))
    except (ValueError, TypeError):
        return "# **Error:** Invalid numeric input.", None

    total, class_name, ratings = compute_rmr(ucs, rqd, spacing, joint_condition, groundwater)

    # Build color-coded badge HTML
    colors = {
        'Class I': '#1b8a2d',  # green
        'Class II': '#7bbf5a',
        'Class III': '#f0e442', # yellow
        'Class IV': '#f0945a',  # orange
        'Class V': '#d62728'    # red
    }
    badge_color = colors.get(class_name, '#888888')
    badge_html = f'<span style="background-color:{badge_color}; color:white; padding:4px 12px; border-radius:8px; font-size:1.2rem; font-weight:bold">{class_name}</span>'

    # Markdown output: large total + badge
    markdown_text = f"# **{total}**\n\n{badge_html}"

    # Horizontal bar chart
    labels = ['UCS', 'RQD', 'Joint Spacing', 'Joint Condition', 'Groundwater']
    plt.figure(figsize=(6, 3.5))
    bars = plt.barh(labels, ratings, color=['#2c7bb6', '#abd9e9', '#fdae61', '#f46d43', '#d73027'])
    plt.xlim(0, 100)
    plt.xlabel('Rating')
    plt.title('RMR Parameter Contributions')
    for bar, val in zip(bars, ratings):
        plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, str(val),
                 va='center', fontsize=10)
    plt.tight_layout()
    fig = plt.gcf()
    plt.close()
    return markdown_text, fig

with gr.Blocks(title="Rock Mass Rating (RMR) Calculator") as demo:
    gr.Markdown("# Rock Mass Rating (RMR) Calculator")
    gr.Markdown("Based on Bieniawski's classification system. Fill in all parameters to compute RMR.")

    with gr.Column():
        ucs_input = gr.Number(label="Intact Rock Strength (UCS) [MPa]", value=10.0, minimum=0.1, maximum=400, step=0.1)
        rqd_input = gr.Slider(label="RQD (%)", minimum=0, maximum=100, value=50, step=1)
        spacing_input = gr.Number(label="Joint Spacing [m]", value=0.5, minimum=0.001, maximum=10, step=0.001)
        joint_condition_input = gr.Dropdown(
            choices=[
                'Very rough surfaces, no separation, hard joint wall',
                'Slightly rough surfaces, <1 mm separation, hard joint wall',
                'Smooth surfaces or 1–5 mm separation',
                'Slickensided or 5–10 mm separation, soft joint wall',
                'Soft gouge >10 mm separation'
            ],
            value='Very rough surfaces, no separation, hard joint wall',
            label="Joint Condition"
        )
        groundwater_input = gr.Dropdown(
            choices=['Completely dry', 'Damp', 'Wet', 'Dripping', 'Flowing'],
            value='Completely dry',
            label="Groundwater Conditions"
        )
        compute_btn = gr.Button("Compute RMR")
        total_output = gr.Markdown(label="Result")
        plot_output = gr.Plot(label="Contributions")

    compute_btn.click(
        fn=rmr_interface,
        inputs=[ucs_input, rqd_input, spacing_input, joint_condition_input, groundwater_input],
        outputs=[total_output, plot_output]
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
