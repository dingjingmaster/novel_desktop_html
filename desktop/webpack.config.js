var CopyPlugin = require('copy-webpack-plugin');
var sourcePath = __dirname + '/app/';
var distPath = __dirname + '/public_html/';
module.exports = {
    mode: 'development',
    devtool: 'source-map',
    entry: {
        index: __dirname + '/app/js/index.js'
    },
    output: {
        path: __dirname + '/public_html/js/',
        filename: '[name].js',
    },
    plugins: [
        new CopyPlugin([
            {
                from: sourcePath + '/index.html',
                to: distPath
            },
            {
                from: sourcePath + '/img',
                to: distPath
            }
        ]),
    ]
};
