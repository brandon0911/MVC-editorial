const btnDelete= document.querySelectorAll('.Borrar');
if(btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if(!confirm('¿Seguro que quieres eliminarlo?')){
        e.preventDefault();
      }
    });
  })
}
