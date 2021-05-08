const http = require('http')

const pageNew = `<!doctype html>
<h3>make a new paste</h3>
<form>
  <textarea name="paste"></textarea>
  <br>
  <input type="submit">
</form>
<div id="error"></div>
<script>error.innerHTML=decodeURIComponent(location.hash.slice(1))</script>
`

http.createServer((req, res) => {
  if (req.method !== 'GET') {
    return res.writeHead(405).end()
  }
  const [pathname, query] = req.url.split('?', 2)
  const paste = new URLSearchParams(query).get('paste')
  const sendMsg = msg => res.writeHead(302, { location: `/#${encodeURIComponent(msg)}` }).end()
  if (pathname !== '/') {
    return sendMsg('error: unknown path')
  }
  if (!paste) {
    return res.writeHead(200, {
      'content-type': 'text/html',
      'content-security-policy': 'default-src \'none\'; script-src \'self\' \'sha256-a857n1MW8s/5S6R7Gyc+gFaD9SwMs5eEheAroy0rzWw=\''
    }).end(pageNew)
  }
  res.writeHead(200, {
    'content-type': 'text/html',
    'content-security-policy': 'default-src \'none\''
  }).end(paste)
}).listen(3000, () => console.log('listening'))
