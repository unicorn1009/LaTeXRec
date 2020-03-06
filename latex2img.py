from io import BytesIO

import matplotlib.pyplot as plt


def render_latex(formula, fontsize=12, dpi=300, format_='svg'):
    """Renders LaTeX formula into image."""
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, u'${}$'.format(formula), fontsize=fontsize)
    buffer_ = BytesIO()
    fig.savefig(buffer_, dpi=dpi, transparent=False, format=format_, bbox_inches='tight', pad_inches=0.0)
    plt.close(fig)
    return buffer_.getvalue()
