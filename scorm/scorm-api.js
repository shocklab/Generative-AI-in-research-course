/*
 * MAM5020F SCORM 1.2 page-completion shim.
 *
 * Behaviour:
 *   - When the page loads inside any SCORM 1.2 compliant LMS, this script
 *     locates the LMS's window.API object, calls LMSInitialize, marks the
 *     lesson_status as "completed", commits, and arranges for LMSFinish on
 *     page unload (with the session time tallied).
 *   - When the page is opened OUTSIDE an LMS (the public GitHub Pages site,
 *     the Amathuba source copies, or a local file://), the script silently
 *     no-ops. The same HTML is therefore usable in all three contexts
 *     without modification.
 *
 * Per the SCORM 1.2 RTE specification, the API object can live on the
 * current window's opener chain (window.parent... or window.opener) up
 * to seven levels deep. We walk both paths defensively.
 */
(function () {
  "use strict";

  function findAPI(win) {
    // SCORM 1.2 scan: walk up the parent chain looking for window.API.
    var depth = 0;
    while (win && depth < 10) {
      if (win.API) return win.API;
      if (!win.parent || win.parent === win) break;
      win = win.parent;
      depth++;
    }
    return null;
  }

  function getAPI() {
    // Try the parent chain first, then the opener chain.
    var api = findAPI(window);
    if (api) return api;
    if (window.opener && typeof window.opener !== "undefined") {
      try {
        api = findAPI(window.opener);
        if (api) return api;
      } catch (e) { /* cross-origin opener; ignore */ }
    }
    return null;
  }

  var api = getAPI();
  if (!api) {
    // No SCORM API in scope. Public-site / standalone path.
    return;
  }

  // Tally session time in seconds.
  var startedAt = Date.now();

  function fmtTime(ms) {
    // SCORM 1.2 CMITimespan is "HH:MM:SS" or "HHHH:MM:SS.SS".
    var totalSec = Math.max(0, Math.floor(ms / 1000));
    var h = Math.floor(totalSec / 3600);
    var m = Math.floor((totalSec % 3600) / 60);
    var s = totalSec % 60;
    function pad(n) { return n < 10 ? "0" + n : "" + n; }
    return pad(h) + ":" + pad(m) + ":" + pad(s);
  }

  function ok(rc) { return rc === "true" || rc === true; }

  try {
    if (ok(api.LMSInitialize(""))) {
      // Set per-page completion: opening the page counts as completing it.
      // (Per the course author's choice. Refine later if quizzes are added.)
      api.LMSSetValue("cmi.core.lesson_status", "completed");
      api.LMSCommit("");
    }
  } catch (e) {
    // Swallow LMS errors so we never disrupt page rendering.
    if (window.console) console.warn("SCORM init failed:", e);
  }

  function finish() {
    try {
      api.LMSSetValue("cmi.core.session_time", fmtTime(Date.now() - startedAt));
      api.LMSCommit("");
      api.LMSFinish("");
    } catch (e) {
      if (window.console) console.warn("SCORM finish failed:", e);
    }
  }

  // Use beforeunload + pagehide for reliability across browsers.
  window.addEventListener("beforeunload", finish);
  window.addEventListener("pagehide", finish);
})();
