
https://www.npmjs.com/package/angular-jsdoc

https://github.com/krampstudio/grunt-jsdoc


http://hashbang.nl/angular/2015/02/10/simple-and-clear-angular-application-documentation-using-angular-jsdoc



install

npm install --save grunt grunt-jsdoc angular-jsdoc


grunt 설정 파일

```

module.exports = function(grunt) {
    'use strict';

    require('load-grunt-tasks')(grunt);

    // Project configuration.
    grunt.initConfig({

        clean: {
            options: {
                force : true
            },
            test: ['doc']
        },

        jsdoc: {
            basic: {
                src: ['./client/pages/main/controllers/*.js', './client/pages/main/services/*.js'],
                options: {
                    destination: 'doc/basic',
                    readme: './README.md'
                }
            }
        }
    });

    // Load local tasks.
    // grunt.loadTasks('tasks');


    //testing tasks
    grunt.registerTask('test-basic',     'Test basic jsdoc', ['jsdoc:basic', 'nodeunit:basic']);
    grunt.registerTask('test-alternate', 'Test jsdoc with alternate options', ['jsdoc:alternate', 'nodeunit:alternate']);
    grunt.registerTask('test-docstrap',  'Test jsdoc with a template', ['jsdoc:docstrap', 'nodeunit:docstrap']);
    grunt.registerTask('test-spacepack', 'Test jsdoc with a package and spaces in the paths', ['jsdoc:spacepack', 'nodeunit:spacepack']);
    grunt.registerTask('test-nosrc', 'Test jsdoc without src and dest, only a config', ['jsdoc:nosrc', 'nodeunit:nosrc']);
    grunt.registerTask('test',           'Full test suite', ['clean:test', 'nodeunit:unit', 'test-basic', 'test-alternate', 'test-docstrap', 'test-spacepack', 'test-nosrc']);

    grunt.registerTask('default', 'Default task will lint and test', ['eslint:all', 'test']);
};

```


jsdoc 예제
```
/**
 * <b>변환식 페이지 컨트롤러</b><br>
 * 변환식 검색/삭제<br>
 * view : /views/contents/transform.html<br>
 *
 * @class FormulaReferenceCtrl
 */
 
 
 /**
 * 변환식 리스트 조회<br>
 *
 * @function
 */




/** @module referenceManager */


/**
* 레퍼런스 수정
* @function module:referenceManager#updateById
* @param {number} id 레퍼런스 Id
* @param {object} body 레퍼런스 객체
* @param {object} callback
*/
```
