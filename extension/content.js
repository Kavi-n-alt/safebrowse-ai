function getPageText() {
  let text = "";
  const walker = document.createTreeWalker(
    document.body,
    NodeFilter.SHOW_TEXT,
    null,
    false
  );
  
  let node;
  while ((node = walker.nextNode()) && text.length < 5000) {
    const trimmed = node.nodeValue.trim();
    if (trimmed.length > 0) {
      text += trimmed + " ";
    }
  }
  return text;
}

async function analyzePage() {
  const text = getPageText();
  if (!text || text.length < 50) return;

  const url = window.location.href;

  try {
    const response = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ 
        url: url, 
        text: text.substring(0, 3000),
        user_id: "demo_child" 
      })
    });

    const data = await response.json();
    showNotification(data);
  } catch (err) {
    console.log("SafeBrowse: Backend not running");
  }
}

function showNotification(data) {
  const existingBanner = document.getElementById("safebrowse-banner");
  if (existingBanner) existingBanner.remove();

  const banner = document.createElement("div");
  banner.id = "safebrowse-banner";
  banner.style.cssText = `
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 999999;
    padding: 12px 18px;
    border-radius: 8px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 14px;
    color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    max-width: 300px;
  `;

  let bgColor = "#27ae60";
  if (data.risk_score >= 70) bgColor = "#e74c3c";
  else if (data.risk_score >= 40) bgColor = "#f39c12";
  
  banner.style.background = bgColor;
  banner.innerHTML = `
    <strong>SafeBrowse AI</strong><br>
    ${data.category.toUpperCase()} - Risk: ${data.risk_score}/100
  `;

  document.body.appendChild(banner);

  setTimeout(() => {
    if (banner.parentElement) banner.remove();
  }, 7000);
}

setTimeout(analyzePage, 2500);
