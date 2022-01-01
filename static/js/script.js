var farsi = document.getElementById('fa_click'),
    english = document.getElementById('en_click'),
    fa_txt = document.querySelectorAll('#fa'),
    en_txt = document.querySelectorAll('#en'),
    nb_fa = fa_txt.length,
    nb_en = en_txt.length;

farsi.addEventListener('click', function() {
    langue(farsi,english);
}, false);

english.addEventListener('click', function() {
    langue(english,farsi);
}, false);

function langue(langueOn,langueOff){
    if (!langueOn.classList.contains('current_lang')) {
        langueOn.classList.toggle('current_lang');
        langueOff.classList.toggle('current_lang');
    }
    if(langueOn.innerHTML == 'فارسی'){
        afficher(fa_txt, nb_fa);
        cacher(en_txt, nb_en);
    }
    else if(langueOn.innerHTML == 'English'){
        afficher(en_txt, nb_en);
        cacher(fa_txt, nb_fa);
    }
}

function afficher(txt,nb){
    for(var i=0; i < nb; i++){
        txt[i].style.display = 'block';
    }
}
function cacher(txt,nb){
    for(var i=0; i < nb; i++){
        txt[i].style.display = 'none';
    }
}
function init(){
    langue(farsi,english);
}
init();