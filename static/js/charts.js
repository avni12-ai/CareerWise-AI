/**
 * CareerWise AI - Visualizations using Chart.js
 * Renders Radar Skill Gap chart and Comparative Career Suitability Bar chart.
 */

window.renderCareerCharts = function(chartData) {
    if (!chartData) return;

    // 1. Radar Chart: Assessed vs Benchmark for Top 1 Career
    const radarCtx = document.getElementById("skillRadarChart");
    if (radarCtx && chartData.radar_top_1) {
        new Chart(radarCtx, {
            type: "radar",
            data: chartData.radar_top_1,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    r: {
                        angleLines: { color: "rgba(0, 0, 0, 0.1)" },
                        grid: { color: "rgba(0, 0, 0, 0.08)" },
                        pointLabels: {
                            font: { family: "'Plus Jakarta Sans', sans-serif", size: 12, weight: "600" },
                            color: "#334155"
                        },
                        suggestedMin: 0,
                        suggestedMax: 5,
                        ticks: { stepSize: 1, backdropColor: "transparent", color: "#64748b" }
                    }
                },
                plugins: {
                    legend: {
                        position: "top",
                        labels: {
                            font: { family: "'Plus Jakarta Sans', sans-serif", size: 12, weight: "600" },
                            padding: 15
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return ` ${context.dataset.label}: Level ${context.raw} / 5`;
                            }
                        }
                    }
                }
            }
        });
    }

    // 2. Bar Chart: Multi-criteria Comparison Across All Evaluated Careers
    const barCtx = document.getElementById("careerComparisonBarChart");
    if (barCtx && chartData.bar_comparison) {
        new Chart(barCtx, {
            type: "bar",
            data: chartData.bar_comparison,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: 'y', // Horizontal bars for clean reading of career titles
                scales: {
                    x: {
                        suggestedMin: 0,
                        suggestedMax: 100,
                        ticks: {
                            callback: function(val) { return val + "%"; },
                            color: "#64748b"
                        },
                        grid: { color: "rgba(0,0,0,0.06)" }
                    },
                    y: {
                        ticks: {
                            font: { family: "'Plus Jakarta Sans', sans-serif", weight: "600" },
                            color: "#1e293b"
                        },
                        grid: { display: false }
                    }
                },
                plugins: {
                    legend: {
                        position: "top",
                        labels: {
                            font: { family: "'Plus Jakarta Sans', sans-serif", size: 12, weight: "600" }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return ` ${context.dataset.label}: ${context.raw}%`;
                            }
                        }
                    }
                }
            }
        });
    }
};
