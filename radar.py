import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Labels for the 7 axes
labels = [
    "Technology & IP",
    "Research & Development",
    "Marketing",
    "Funding & Financials",
    "Industrialization & Partnerships"
]

# Values (EDIT HERE)
current = [8, 9, 3, 5, 5]
target  = [9, 9, 8, 7, 8]

# Close the loop by repeating the first value
current += current[:1]
target += target[:1]

# Calculate angles
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

# Setup figure
fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))

# Plot current
ax.plot(angles, current, linewidth=2, linestyle='solid', label='Current', color='tab:blue')
ax.fill(angles, current, alpha=0.25, color='tab:blue')

# Plot target
ax.plot(angles, target, linewidth=2, linestyle='dashed', label='Target', color='tab:orange')
ax.fill(angles, target, alpha=0.15, color='tab:orange')

# Customize radar chart
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
ax.set_ylim(0, 10)
ax.set_rlabel_position(180 / len(labels))
ax.set_title(" ", size=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Show in Streamlit
st.pyplot(fig)
