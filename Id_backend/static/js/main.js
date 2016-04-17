$(function () {
    $("#image-input-1:file").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = imageIsLoaded_1;
            reader.readAsDataURL(this.files[0]);
        }
    });
    $("#image-input-2:file").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = imageIsLoaded_2;
            reader.readAsDataURL(this.files[0]);
        }
    });
});

function imageIsLoaded_1(e) {
    $('#uploaded-img-1').attr('src', e.target.result);
};
function imageIsLoaded_2(e) {
    $('#uploaded-img-2').attr('src', e.target.result);
};


$(function () {
    "use strict";
            
    $('#detect-1').click(function (e) {
        e.preventDefault();

        $(this).find('.face').remove();

        $('#picture-1').faceDetection({
            complete: function (faces) {
                console.log(faces);
                
                for (var i = 0; i < faces.length; i++) {
                    $('<div>', {
                        'class':'face',
                        'css': {
                            'position': 'absolute',
                            'left':     faces[i].x * faces[i].scaleX + 'px',
                            'top':      faces[i].y * faces[i].scaleY + 'px',
                            'width':    faces[i].width  * faces[i].scaleX + 'px',
                            'height':   faces[i].height * faces[i].scaleY + 'px'
                        }
                    })
                    .insertAfter(this);
                }
            },
            error:function (code, message) {
                alert('Error: ' + message);
            }
        });
    });

    $('#reset-1').click(function (e) {
        e.preventDefault();
        $(this).closest('.picture-container').find('.face').remove();
    });


    $('#detect-2').click(function (e) {
        e.preventDefault();

        $(this).find('.face').remove();

        $('#picture-2').faceDetection({
            complete: function (faces) {
                console.log(faces);
                
                for (var i = 0; i < faces.length; i++) {
                    $('<div>', {
                        'class':'face',
                        'css': {
                            'position': 'absolute',
                            'left':     faces[i].x * faces[i].scaleX + 'px',
                            'top':      faces[i].y * faces[i].scaleY + 'px',
                            'width':    faces[i].width  * faces[i].scaleX + 'px',
                            'height':   faces[i].height * faces[i].scaleY + 'px'
                        }
                    })
                    .insertAfter(this);
                }
            },
            error:function (code, message) {
                alert('Error: ' + message);
            }
        });
    });
    $('#reset-2').click(function (e) {
        e.preventDefault();
        $(this).closest('.picture-container').find('.face').remove();
    });


    $('#detect-3').click(function (e) {
        e.preventDefault();

        $(this).find('.face').remove();

        $('#picture-3').faceDetection({
            complete: function (faces) {
                console.log(faces);
                
                for (var i = 0; i < faces.length; i++) {
                    $('<div>', {
                        'class':'face',
                        'css': {
                            'position': 'absolute',
                            'left':     faces[i].x * faces[i].scaleX + 'px',
                            'top':      faces[i].y * faces[i].scaleY + 'px',
                            'width':    faces[i].width  * faces[i].scaleX + 'px',
                            'height':   faces[i].height * faces[i].scaleY + 'px'
                        }
                    })
                    .insertAfter(this);
                }
            },
            error:function (code, message) {
                alert('Error: ' + message);
            }
        });
    });

$('#reset-3').click(function (e) {
    e.preventDefault();
    $(this).closest('.picture-container').find('.face').remove();
});

//for image uploading
    $('#detect-upload-1').click(function (e) {
        e.preventDefault();

        $(this).find('.face').remove();

        $('#uploaded-img-1').faceDetection({
            complete: function (faces) {
                console.log(faces);
                
                for (var i = 0; i < faces.length; i++) {
                    $('<div>', {
                        'class':'face',
                        'css': {
                            'position': 'absolute',
                            'left':     faces[i].x * faces[i].scaleX + 'px',
                            'top':      faces[i].y * faces[i].scaleY + 'px',
                            'width':    faces[i].width  * faces[i].scaleX + 'px',
                            'height':   faces[i].height * faces[i].scaleY + 'px'
                        }
                    })
                    .insertAfter(this);
                }
            },
            error:function (code, message) {
                alert('Error: ' + message);
            }
        });
    });
    $('#reset-upload-1').click(function (e) {
        e.preventDefault();
        $(this).closest('.picture-container').find('.face').remove();
    });

    $('#detect-upload-2').click(function (e) {
        e.preventDefault();

        $(this).find('.face').remove();

        $('#uploaded-img-2').faceDetection({
            complete: function (faces) {
                console.log(faces);
                
                for (var i = 0; i < faces.length; i++) {
                    $('<div>', {
                        'class':'face',
                        'css': {
                            'position': 'absolute',
                            'left':     faces[i].x * faces[i].scaleX + 'px',
                            'top':      faces[i].y * faces[i].scaleY + 'px',
                            'width':    faces[i].width  * faces[i].scaleX + 'px',
                            'height':   faces[i].height * faces[i].scaleY + 'px'
                        }
                    })
                    .insertAfter(this);
                }
            },
            error:function (code, message) {
                alert('Error: ' + message);
            }
        });
    });
    $('#reset-upload-2').click(function (e) {
        e.preventDefault();
        $(this).closest('.picture-container').find('.face').remove();
    });
});