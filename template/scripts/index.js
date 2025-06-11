  document.getElementById('login-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    const response = await fetch('http://127.0.0.1:8001/login', {
      method: 'POST',
      body: formData
    });
    if (response.ok) {
      window.location.href = '/template/home.html'
      alert('Login realizado com sucesso!');
    } else {
      const errorText = await response.json();
      alert('Erro ao fazer login: ' + errorText.detail);
    }
  });
