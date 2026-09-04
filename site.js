document.documentElement.classList.add('js');
const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('in');observer.unobserve(entry.target)}}),{threshold:.14});
document.querySelectorAll('[data-reveal]').forEach(el=>observer.observe(el));
const progress=document.querySelector('.progress span');
const update=()=>{const max=document.documentElement.scrollHeight-innerHeight;progress.style.width=(max>0?(scrollY/max)*100:0)+'%'};
addEventListener('scroll',update,{passive:true});addEventListener('resize',update);update();
