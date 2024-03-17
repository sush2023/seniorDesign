// document.getElementById('inputForm').addEventListener('submit', function(event)
function token_callback(event)
{
    console.log("detected click")
    //event.preventDefault();
    //var token = document.getElementById('token').value;
    var token= "random";
    let calibration_state;
    fetch('/process', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ token: token}),
    })
    .then(response => response.json())
    .then()
    .then(data => {
      console.log("data.calibration_state: ", data.calibration_state);
      if (data.calibration_state)
        window.location.href = "/calibration"
    })
    .catch(error => {
      console.error('Error:', error);
    });
    console.log("calibration_state is:", calibration_state)
    
};
  