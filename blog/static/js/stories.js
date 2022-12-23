/*! stories.js | Friendkit | © Css Ninja. 2019-2020 */

/* ==========================================================================
Stories functions
========================================================================== */
"use strict";

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }



$(document).ready(function () {
  //Sidebar
  if ($('.stories-sidebar').length) {
    var handleMobileSidebar = function handleMobileSidebar() {
      if (window.matchMedia("(max-width: 767px)").matches) {
        $('.stories-sidebar').removeClass('is-active');
      } else if (window.matchMedia("(max-width: 768px)").matches) {
        $('.stories-sidebar').removeClass('is-active');
      } else {
        $('.stories-sidebar').addClass('is-active');
      }
    };

    $('.mobile-sidebar-trigger').on('click', function () {
      $('.stories-sidebar').addClass('is-active');
    });
    $('.close-stories-sidebar').on('click', function () {
      $(this).closest('.stories-sidebar').removeClass('is-active');
    });
    handleMobileSidebar();
    $(window).on('resize', function () {
      handleMobileSidebar();
    });
  }

  initAutoTag(); //Close selection modal

  $('.new-story-modal .selection-box').on('click', function () {
    $(this).closest('.modal').removeClass('is-active');
  });

  function deletePreview() {
    $('.delete-preview-item').off().on('click', function () {
      $('.preview-image-container').remove();
      $('.upload-placeholder, .image-upload-placeholder').removeClass('is-hidden');
      $('#story-upload, #image-story-upload').val('');
    });
  }

  if ($('#story-upload').length) {
    document.getElementById('story-upload').addEventListener('change', function (event) {
      var file = event.target.files[0];
      var fileReader = new FileReader();

      if (file.type.match('image')) {
        toasts.service.info('', 'mdi mdi-video', 'Please upload a video file', 'bottomRight', 2500);
        document.getElementById('story-upload').value = null;
      } else {
        fileReader.onload = function () {
          var blob = new Blob([fileReader.result], {
            type: file.type
          });
          var url = URL.createObjectURL(blob);
          var video = document.createElement('video');

          var timeupdate = function timeupdate() {
            if (snapImage()) {
              video.removeEventListener('timeupdate', timeupdate);
              video.pause();
            }
          };

          video.addEventListener('loadeddata', function () {
            if (snapImage()) {
              video.removeEventListener('timeupdate', timeupdate);
            }
          });

          var snapImage = function snapImage() {
            var canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
            var image = canvas.toDataURL();
            var success = image.length > 100000;

            if (success) {
              var img = "\n                                <div id=\"video-preview-container\" class=\"preview-image-container\">\n                                    <button class=\"delete delete-preview-item\"></button>\n                                    <img class=\"preview-image\" src=\"" + image + "\" alt=\"\">\n                                </div>\n                            ";
              document.getElementById('video-upload-placeholder').classList.add('is-hidden');
              document.getElementById('preview').insertAdjacentHTML('beforeend', img);
              deletePreview();
              URL.revokeObjectURL(url);
            }

            return success;
          };

          video.addEventListener('timeupdate', timeupdate);
          video.preload = 'metadata';
          video.src = url; // Load video in Safari / IE11

          video.muted = true;
          video.playsInline = true;
          video.play();
        };

        fileReader.readAsArrayBuffer(file);
      }

      var fileEl = document.getElementById('story-upload');
      console.log(fileEl.files);
    });
  }

  if ($('#story-image-upload').length) {
    document.getElementById('image-story-upload').addEventListener('change', function (event) {
      var file = event.target.files[0];
      var fileReader = new FileReader();

      if (file.type.match('image')) {
        fileReader.onload = function () {
          var img = "\n                        <div id=\"image-preview-container\" class=\"preview-image-container\">\n                            <button class=\"delete delete-preview-item\"></button>\n                            <img class=\"preview-image\" src=\"" + fileReader.result + "\" alt=\"\">\n                        </div>\n                    ";
          document.getElementById('image-upload-placeholder').classList.add('is-hidden');
          document.getElementById('image-preview').insertAdjacentHTML('beforeend', img);
          deletePreview();
        };

        fileReader.readAsDataURL(file);
      } else {
        toasts.service.info('', 'mdi mdi-image-outline', 'Please upload an image', 'bottomRight', 2500);
        document.getElementById('image-story-upload').value = null;
      }

      var fileEl = document.getElementById('image-story-upload');
      console.log(fileEl.files);
    });
  }
});