(function(){
  const htmlEl = document.documentElement;

  function initLucide(){ try { window.lucide?.createIcons?.(); } catch(e) { console.warn(e); } }

  function initDarkMode(){
    const saved = localStorage.getItem('theme');
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const isDark = saved ? saved === 'dark' : prefersDark;
    if (isDark) htmlEl.classList.add('dark'); else htmlEl.classList.remove('dark');
  }

  function createFloatingToggle(){
    if (document.getElementById('dark-mode-toggle')) return;
    const header = document.querySelector('header');
    if (!header) return;

    const wrapper = document.createElement('div');
    wrapper.className = 'floating-dark-toggle-wrapper';
    wrapper.innerHTML = `
      <button id="dark-mode-toggle" aria-label="Toggle dark mode" class="relative w-14 h-8 bg-gray-200 dark:bg-gray-700 rounded-full shadow-inner transition-colors focus:outline-none">
        <span id="toggle-handle" class="absolute left-0 top-0.5 w-7 h-7 bg-white rounded-full shadow transform transition-transform duration-300 flex items-center justify-center">
          <i data-lucide="sun" class="w-4 h-4 block dark:hidden text-yellow-500"></i>
          <i data-lucide="moon" class="w-4 h-4 hidden dark:block text-gray-900"></i>
        </span>
      </button>
    `;
    header.insertAdjacentElement('afterend', wrapper);
  }

  function wireDarkToggle(){
    const btn = document.getElementById('dark-mode-toggle');
    const handle = document.getElementById('toggle-handle');
    if (!btn) return;

    function setHandlePosition(isDark){
      if (!handle) return;
      if (isDark) handle.classList.add('translate-x-6');
      else handle.classList.remove('translate-x-6');
    }

    setHandlePosition(htmlEl.classList.contains('dark'));
    btn.addEventListener('click', (e)=>{
      e.stopImmediatePropagation();
      htmlEl.classList.toggle('dark');
      const nowDark = htmlEl.classList.contains('dark');
      localStorage.setItem('theme', nowDark ? 'dark' : 'light');
      setHandlePosition(nowDark);
      try { window.lucide?.createIcons?.(); } catch {}
    }, { capture: true });
  }

  function initRetractingHeader(){
    const header = document.querySelector('header');
    if (!header) return;
    header.classList.add('retractable');
    let lastScroll = window.scrollY || 0;
    let ticking = false;
    function onScroll(){
      const current = window.scrollY || 0;
      const delta = current - lastScroll;
      if (Math.abs(delta) < 10) return;
      if (delta > 0 && current > 80) header.classList.add('is-hidden');
      else if (delta < 0) header.classList.remove('is-hidden');
      lastScroll = current;
      ticking = false;
    }
    window.addEventListener('scroll', ()=>{ if(!ticking){ requestAnimationFrame(onScroll); ticking=true; } }, { passive:true });
  }

  function wireTocToggle(){
    const toc = document.getElementById('toc');
    const tocToggleBtn = document.getElementById('toc-toggle');
    const tocOpenBtn = document.getElementById('toc-open-btn');
    if (!toc) return;

    const setCollapsed = (collapsed) => {
      if (collapsed) toc.classList.add('toc-collapsed');
      else toc.classList.remove('toc-collapsed');
    };

    if (tocToggleBtn){
      tocToggleBtn.setAttribute('aria-expanded', String(!toc.classList.contains('toc-collapsed')));
      tocToggleBtn.addEventListener('click', ()=>{
        const collapsed = toc.classList.toggle('toc-collapsed');
        tocToggleBtn.setAttribute('aria-expanded', String(!collapsed));
        setCollapsed(collapsed);
      });
    }

    if (tocOpenBtn){
      tocOpenBtn.addEventListener('click', ()=>{
        setCollapsed(false);
        tocToggleBtn?.setAttribute('aria-expanded','true');
        const firstLink = toc.querySelector('a');
        if(firstLink) firstLink.focus();
      });
    }
  }

  function init(){
    initDarkMode();
    createFloatingToggle();
    initLucide();
    wireDarkToggle();
    initRetractingHeader();
    wireTocToggle();
  }

  window.__headerInit = init;
  if (document.readyState==='loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();


document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('search-toggle');
    const dropdown = document.getElementById('search-dropdown');
    const input = document.getElementById('search-input');

    // Toggle visibility
    toggle.addEventListener('click', () => {
        dropdown.classList.toggle('hidden');
        if (!dropdown.classList.contains('hidden')) {
            input.focus();
        }
    });

    // Press Enter → redirect to search.html with query
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const query = encodeURIComponent(input.value.trim());
            if (query) {
                window.location.href = `search.html?q=${query}`;
            }
        }
    });

    // Optional: hide dropdown if clicked outside
    document.addEventListener('click', (e) => {
        if (!dropdown.contains(e.target) && !toggle.contains(e.target)) {
            dropdown.classList.add('hidden');
        }
    });
});

