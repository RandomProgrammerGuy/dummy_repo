require('dotenv').config();

const express = require('express');
const expressLayout = require('express-ejs-layouts')

const app = express()
const PORT = 31415 || process.env.PORT;

app.use(express.static('public'))

// Templating Engine
app.use(expressLayout);
app.set('layout', './layouts/main');
app.set('viewengine', 'ejs')

app.use('/', require('./server/routes/main'))

app.listen(PORT, ()=> {
    console.log('app listening on port 31415')
});