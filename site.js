document.documentElement.classList.add('js');
const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('in');observer.unobserve(entry.target)}}),{threshold:.14});
document.querySelectorAll('[data-reveal]').forEach(el=>observer.observe(el));
const progress=document.querySelector('.progress span');
const update=()=>{const max=document.documentElement.scrollHeight-innerHeight;progress.style.width=(max>0?(scrollY/max)*100:0)+'%'};
addEventListener('scroll',update,{passive:true});addEventListener('resize',update);update();

document.querySelectorAll('.menu-toggle').forEach(button=>{
  button.addEventListener('click',()=>{
    const nav=button.closest('.nav');
    const open=nav.classList.toggle('nav-open');
    button.setAttribute('aria-expanded',String(open));
    button.querySelector('.sr-only').textContent=open?'Close navigation':'Open navigation';
  });
  button.closest('.nav').querySelectorAll('.nav-links a').forEach(link=>link.addEventListener('click',()=>{
    const nav=button.closest('.nav');nav.classList.remove('nav-open');button.setAttribute('aria-expanded','false');button.querySelector('.sr-only').textContent='Open navigation';
  }));
});
addEventListener('keydown',event=>{if(event.key==='Escape')document.querySelectorAll('.nav-open').forEach(nav=>{nav.classList.remove('nav-open');const button=nav.querySelector('.menu-toggle');if(button){button.setAttribute('aria-expanded','false');button.querySelector('.sr-only').textContent='Open navigation'}})});
