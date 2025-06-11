  document.getElementById('cadastro-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    const response = await fetch('http://127.0.0.1:8001/cadastro', {
      method: 'POST',
      body: formData
    });
    if (response.ok) {
      window.location.href = '/template/index.html'
      alert('Cadastro realizado com sucesso! Você pode fazer login agora.');
    } else {
      const errorText = await response.json();
      alert('Erro ao fazer cadastro: ' + errorText.detail);
    }
  });
