document.getElementById('inputForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var name = document.getElementById('name').value;
    var age = document.getElementById('age').value;
  
    fetch('/process', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: name, age: age }),
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('result').innerText = data.message;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
  