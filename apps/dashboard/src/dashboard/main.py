"""KwiekEnergie Energy Dashboard — Streamlit application."""

import logging

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

logger = logging.getLogger(__name__)


def build_monthly_data() -> pd.DataFrame:
    """Return sample monthly energy data for the dashboard."""
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    solar_kwh = [120, 145, 310, 430, 520, 590, 610, 570, 400, 250, 140, 100]
    grid_kwh = [380, 320, 200, 140, 90, 60, 50, 70, 130, 230, 360, 400]
    return pd.DataFrame(
        {"Month": months, "Solar (kWh)": solar_kwh, "Grid (kWh)": grid_kwh}
    )


def render_kpi_row(df: pd.DataFrame) -> None:
    """Render top-level KPI metric cards."""
    total_solar = int(df["Solar (kWh)"].sum())
    total_grid = int(df["Grid (kWh)"].sum())
    total_kwh = total_solar + total_grid
    solar_share = round(total_solar / total_kwh * 100, 1)
    cost_saving = round(total_solar * 0.32, 0)  # €0.32 per kWh avoided

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total consumption", f"{total_kwh:,} kWh")
    col2.metric("Solar generation", f"{total_solar:,} kWh")
    col3.metric("Solar share", f"{solar_share} %")
    col4.metric("Estimated savings", f"€ {cost_saving:,.0f}")


def render_energy_chart(df: pd.DataFrame) -> None:
    """Render a stacked bar chart of monthly solar vs. grid consumption."""
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name="Solar (kWh)",
            x=df["Month"],
            y=df["Solar (kWh)"],
            marker_color="#F5A623",
        )
    )
    fig.add_trace(
        go.Bar(
            name="Grid (kWh)",
            x=df["Month"],
            y=df["Grid (kWh)"],
            marker_color="#4A90D9",
        )
    )

    fig.update_layout(
        barmode="stack",
        title="Monthly energy mix",
        xaxis_title="Month",
        yaxis_title="kWh",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        plot_bgcolor="white",
        paper_bgcolor="white",
    )
    st.plotly_chart(fig, width="stretch")


def main() -> None:
    """Run the Streamlit energy dashboard."""
    st.set_page_config(
        page_title="Kwiek Energie — Energy Dashboard",
        page_icon="⚡",
        layout="wide",
    )

    st.title("⚡ Kwiek Energie — Energy Dashboard")
    st.caption("Sample overview of annual energy production and consumption.")

    st.divider()

    df = build_monthly_data()

    render_kpi_row(df)

    st.divider()

    render_energy_chart(df)

    st.divider()

    st.subheader("Monthly data")
    st.dataframe(df.set_index("Month"), width="stretch")

    st.caption("© Kwiek Energie BV — data shown is for demonstration purposes only.")
    logger.info("Dashboard rendered successfully")


if __name__ == "__main__":
    main()
