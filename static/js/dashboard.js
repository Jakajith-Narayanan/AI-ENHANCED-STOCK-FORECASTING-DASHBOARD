const form = document.getElementById('form');
const results = document.getElementById('results');
const sentimentJson = document.getElementById('sentimentJson');
const gptSummary = document.getElementById('gptSummary');
const rec = document.getElementById('recommendation');
let chart;

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const symbol = document.getElementById('symbol').value;
  const pdf = document.getElementById('pdf').files[0];

  const fd = new FormData();
  fd.append('symbol', symbol);
  fd.append('pdf', pdf);

  const res = await fetch('/api/analyze', {
    method: 'POST',
    body: fd
  });

  const data = await res.json();

    if (data.error) {
    alert("❌ Error: " + data.error);
    return;
  }

  // Update chart
  const ctx = document.getElementById('forecastChart').getContext('2d');
  if (chart) chart.destroy();
  chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.forecast_dates,
      datasets: [{
        label: 'Forecast Price',
        data: data.forecast_values,
        borderColor: 'rgba(0, 123, 255, 1)',
        backgroundColor: 'rgba(0, 123, 255, 0.1)',
        fill: true,
        tension: 0.3
      }]
    }
  });

  sentimentJson.textContent = JSON.stringify(data.sentiment, null, 2);
  gptSummary.textContent = data.gpt_summary;
  rec.textContent = `✅ Final Recommendation: ${data.decision} (score: ${data.score})`;
  document.getElementById('companyName').textContent = `📈 Company Analyzed: ${data.company}`;

  results.style.display = 'block';
});
