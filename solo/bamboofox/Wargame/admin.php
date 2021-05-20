<?php
    session_start();

    $flag = shell_exec('cat /flag*');
    $action = @$_GET['action'];
    
    if ($action == 'login') {
        $username = @$_POST['username'];
        $password = @$_POST['password'];

        if (!$username) die('no username');
        if (!$password) die('no password');

        if (strcmp($password, md5($flag)) != 0)
            die('wrong password');
        
        $_SESSION['user'] = $username;
    }
    else if ($action == 'logout') {
        unset($_SESSION['user']);
    }
?>

<?php if (!isset($_SESSION['user'])): ?>
    <form action="?action=login" method="post">
        <b>Admin Login</b><br>
        <input type="text" name="username" value="admin"><br>
        <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
<?php else: ?>
    <form action="?action=logout">
        <h3>Welcome, <?= $_SESSION['user'] ?>, this admin panel is garbage.</h3>
        <b><?php $flag = shell_exec('cat /flag*'); ?></b><br>
        <input type="input" value="<?= htmlentities($flag) ?>">
        <input type="submit" value="Logout">
    </form>
<?php endif; ?>

