old_code = '''      // Sync state when logging in via form
      var loginForm = document.getElementById("loginForm");
      if (loginForm) {
        loginForm.addEventListener("submit", function () {
          var idVal = (document.getElementById("applicantIdInput") || {}).value || "";
          var pwVal = (document.getElementById("applicantPwInput") || {}).value || "";
          var idClean = idVal.trim().toUpperCase();
          if ((idClean === "UC-2027-89321" || idClean === "DUBEY351DEV@GMAIL.COM") && pwVal === "9833@dEVuc") {
            sessionStorage.setItem("applicantLoggedIn", "true");
            if (portalTopBanner) portalTopBanner.style.display = "none";
          }
        });
      }'''

new_code = '''      // Sync state when logging in via form
      var loginForm = document.getElementById("loginForm");
      if (loginForm) {
        loginForm.addEventListener("submit", function (e) {
          e.preventDefault();
          var idInput = document.getElementById("applicantIdInput");
          var pwInput = document.getElementById("applicantPwInput");
          var idVal = (idInput ? idInput.value : "").trim().toUpperCase();
          var pwVal = (pwInput ? pwInput.value : "").trim();
          var notice = document.getElementById("portalNotice");

          var validIds = ["UC-2027-89321", "UCH-2027-88419", "DUBEY351DEV@GMAIL.COM", "D.DUBEY.PHD@UCHICAGO.EDU"];
          var validPws = ["9833@dEVuc", "9833@devuc"];

          if (validIds.indexOf(idVal) !== -1 && validPws.indexOf(pwVal) !== -1) {
            sessionStorage.setItem("applicantLoggedIn", "true");
            if (notice) notice.style.display = "none";
            if (portalLoginView) portalLoginView.style.display = "none";
            if (portalDashboardView) portalDashboardView.style.display = "block";
            if (portalTopBanner) portalTopBanner.style.display = "none";
            if (portalTitle) portalTitle.textContent = "Welcome, Devendra Biswambhar Nath Dubey";
            window.scrollTo({ top: 0, behavior: "smooth" });
          } else {
            if (notice) {
              notice.innerHTML = '<i class="fa-solid fa-triangle-exclamation" style="margin-right: 6px;"></i> Invalid Application ID or Password. Please check your credentials and try again.';
              notice.style.display = "block";
              notice.style.background = "#fff5f5";
              notice.style.color = "#c53030";
              notice.style.border = "1px solid #feb2b2";
              notice.style.padding = "10px 14px";
              notice.style.borderRadius = "4px";
              notice.style.fontSize = "13px";
              notice.style.marginBottom = "14px";
            }
          }
        });
      }'''

for path in ['site_1to1/portal.html', 'site_1to1/pages/portal.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # normalize CRLF for replacement
    text_norm = text.replace('\r\n', '\n')
    old_norm = old_code.replace('\r\n', '\n')
    new_norm = new_code.replace('\r\n', '\n')
    
    if old_norm in text_norm:
        text_norm = text_norm.replace(old_norm, new_norm)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text_norm)
        print(f"Updated {path} successfully!")
    else:
        print(f"Could not find old_code in {path}")
