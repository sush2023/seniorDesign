// document.getElementById('inputForm').addEventListener('submit', function(event)
function token_callback(event)
{
  // var url = window.location.protocol + "//" + window.location.hostname;
  // if (window.location.port) {
  //     url += ":" + window.location.port;
  // }
  // url += "/notification.html";
  // url = url.split('?')[0];
  // setTimeout(function(){document.location.href = url},500);
  // console.log("href is", window.location.href);
  fetch('/notification', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      }
    })
  .then(window.location.href = "{{ url_for('notification') }}");
    // 
    // .then(response => response.json())
    // .then(data => {
    //   console.log("data.calibration_state: ", data.calibration_state);
    //   window.location.href = "/notification";
    // })
    // .catch(error => {
    //   console.error('Error:', error);
    // });
    // console.log("calibration_state is:", calibration_state);  
};

function calibration_callback()
{
  window.location.href = "/calibration"  
}

function token_submit_callback()
{
  var token = document.getElementById('user_token').value;
  console.log("token is: ",  token)
  fetch('/processToken', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ token: token}),
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('result').innerText = data.message;
  })
}

function token_submit_acknowledge()
{
  if (document.getElementById('acknowledge').checked)
    console.log("notif worked")
    fetch('/updateStatus',{
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ "function": "Notification", "boolean": "true"}),
    })
}