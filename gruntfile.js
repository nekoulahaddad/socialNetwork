module.exports = function(grunt) {
    grunt.initConfig({
        uncss: {
            dist: {
                files: [{
                    nonull: true,
                    src: ['http://localhost:8000/'],
                    dest: 'apps/static/css/styles.css'
                }]
            }, 
            options: {
                // ignoreSheets : [/fonts.googleapis/, /cdn.jsdelivr.net/],
                // stylesheets: ['/static/styles/styles.css'],
                // 960px
                media : ['(min-width: 668px) handheld and (orientation: landscape)'],
                // media : ['(max-width: 1600px) handheld and (orientation: landscape)'],
            }
        }
    });

    // Load the plugins
    grunt.loadNpmTasks('grunt-uncss');

    // Default tasks.
    grunt.registerTask('default', ['uncss']);

};