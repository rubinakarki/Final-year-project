const mix = require("laravel-mix")
const path = require("path")

mix.setPublicPath(path.normalize("./../static/"))

if (mix.inProduction()) {
    mix.options({
        terser: {
            terserOptions: {
                compress: {
                    drop_console: true,
                },
            },
        },
    })
} else {
    mix.webpackConfig({ devtool: "inline-source-map" }).sourceMaps()
}

function resolve(dir) {
    return path.join(__dirname, dir)
}

mix.webpackConfig({
    resolve: {
        alias: {
            "@": resolve("src/js"),
            "vue$": "vue/dist/vue.js",
        },
    },

    output: {
        publicPath: path.normalize("/"),
        chunkFilename: "[name].js",
    },

    watchOptions: {
        ignored: /node_modules/,
    },
})

mix.js("src/js/app.js", "js/app.js").version()

mix.extract([
    "vue",
])

// mix.autoload({
//     jquery: ["$", "window.jQuery"],
// })

// mix.sass("resources/assets/auth/sass/vendor.scss", "css/vendor.css").version()
// mix.sass("resources/assets/auth/sass/theme.scss", "css/theme.css").version()
// mix.sass("resources/assets/auth/sass/app.scss", "css/app.css").version()