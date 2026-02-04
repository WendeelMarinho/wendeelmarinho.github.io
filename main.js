// Theme toggle with persistence
(() => {
  const root = document.documentElement;
  const themeToggle = document.getElementById('theme-toggle');
  const backToTop = document.getElementById('back-to-top');
  const copyBtns = [document.getElementById('copy-email'), document.getElementById('copy-email-2')].filter(Boolean);
  const email = 'wendeelmarinho@gmail.com';

  // apply saved theme
  const saved = localStorage.getItem('theme');
  if (saved === 'light') root.classList.add('light');

  themeToggle && themeToggle.addEventListener('click', () => {
    const isLight = root.classList.toggle('light');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
  });

  // smooth scroll (ensure enabled)
  document.documentElement.style.scrollBehavior = 'smooth';

  // Active nav highlight using IntersectionObserver
  const links = Array.from(document.querySelectorAll('.nav-links a'));
  const sections = links.map(l => document.querySelector(l.getAttribute('href'))).filter(Boolean);
  if ('IntersectionObserver' in window && sections.length) {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        const id = '#' + e.target.id;
        const link = document.querySelector('.nav-links a[href="' + id + '"]');
        if (e.isIntersecting) {
          links.forEach(a => a.classList.remove('active'));
          link && link.classList.add('active');
        }
      });
    }, {rootMargin: '-40% 0px -40% 0px', threshold: 0});
    sections.forEach(s => obs.observe(s));
  }

  // copy email helper
  async function copyEmail() {
    try {
      await navigator.clipboard.writeText(email);
      showTemporary('Copied email to clipboard');
    } catch (err) {
      showTemporary('Copy failed — use mailto');
    }
  }

  copyBtns.forEach(b => b.addEventListener('click', copyEmail));

  // small temporary toast (accessible)
  function showTemporary(text) {
    const t = document.createElement('div');
    t.className = 'tmp-toast';
    t.setAttribute('role','status');
    t.textContent = text;
    Object.assign(t.style,{position:'fixed',right:'18px',bottom:'80px',background:'#111',color:'#fff',padding:'10px 12px',borderRadius:'8px',zIndex:80});
    document.body.appendChild(t);
    setTimeout(()=>t.remove(),1800);
  }

  // Back to top visibility
  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) backToTop.style.display = 'flex'; else backToTop.style.display = 'none';
  });
  backToTop && backToTop.addEventListener('click', () => window.scrollTo({top:0,behavior:'smooth'}));

  // Basic form guard: since site is static, disable send but enable when fields are filled
  const nameInput = document.getElementById('name');
  const messageInput = document.getElementById('message');
  const sendBtn = document.getElementById('contact-send');
  function checkForm() {
    if (!sendBtn) return;
    sendBtn.disabled = !(nameInput && messageInput && nameInput.value.trim() && messageInput.value.trim());
  }
  [nameInput,messageInput].filter(Boolean).forEach(el => el.addEventListener('input', checkForm));

})();
