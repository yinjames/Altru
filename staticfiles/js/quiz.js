console.log(window.location.href)
const url = window.location.href //'quizes/1'//$(this).attr('href')
const quiz = document.getElementById('quiz')
var quiz_list = []
let data
let consent_url
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response) {
        data = response.data
        consent_url = response.url
        data.forEach(el => {
            for (const [question, options] of Object.entries(el)) {

                //options.pop()
                options_ = options.slice(0, -1)
                opts = ''
                options_.forEach(opt => {
                    opt = opt.split(':')
                    text = opt[0]
                    ans = opt[opt.length - 1]
                    
                    opts += `
                 <button type="button" class="ans btn btn-lg btn-outline-secondary rounded py-3" ans="${ans}">${text}</button>
                 `

                })
                q = `<p class="my-4 lead">${question}</p>` + `<div class="d-grid gap-5">${opts}</div>`

                /*quiz.innerHTML += `
                <div class="card p-5 mb-3 rounded">
                ${q}
                <div>
                `*/
                to_append = `<div class="card p-5 mb-3 rounded">${q}<div>`
                quiz_list.push(to_append)

            }
        });
        quiz.innerHTML = quiz_list[0]
    },
    error: function (error) {
        console.log(error)
    }

})

var i = 1
$(document).on('click', "#next", function () {

    i = parseInt(i)
    if (i < quiz_list.length) {
        quiz.innerHTML = quiz_list[i]
    }

    i = i + 1
});

var nextQuestion = function () {
    i = parseInt(i);
    if (i < quiz_list.length) {
        quiz.innerHTML = quiz_list[i];
    } else {
        let score = $("#quiz").attr("score");
        score = parseInt((score / (100* quiz_list.length)) *100)
        let qs =''
        data.forEach((el, idx) => {
            for (const [question, options] of Object.entries(el)) {
                qs +=`
        <div class="accordion-item">
            <h2 class="accordion-header text-lead" id="flush-heading${idx}">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                data-bs-target="#flush-${idx}" aria-expanded="false"
                aria-controls="flush-collapse${idx}">
                ${question}
            </button>
            </h2>
            <div id="flush-${idx}" class="accordion-collapse collapse"
            aria-labelledby="flush-heading${idx}" data-bs-parent="#accordionFlushExample">
                <div class="accordion-body text-left">
                ${options.pop()}
                </div>
            </div>
        </div>
        `;


            }

            quiz.innerHTML = `
            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-12">
                        <div class="accordion accordion-flush rounded shadow" id="accordionFlushExample">
                        ${qs}
                        </div>
                    </div>
                   
                    <div class="col-md-4 col-12">
                    
                    <div class="bg-white rounded p-5 shadow">
                      <h2 class="h6 font-weight-bold text-center mb-4">Score</h2>
              
                      <!-- Progress bar 1 -->
                      <div class="progress mx-auto" data-value='${score}'>
                        <span class="progress-left">
                                      <span class="progress-bar border-primary"></span>
                        </span>
                        <span class="progress-right">
                                      <span class="progress-bar border-primary"></span>
                        </span>
                        <div class="progress-value w-100 h-100 rounded-circle d-flex align-items-center justify-content-center">
                          <div class="h2 font-weight-bold">${score}<sup class="small">%</sup></div>
                        </div>
                      </div>
                      <!-- END -->
                      <div class="row mt-3 g-2 px-auto">
                      <p>Will You give consent to donate your organs after death?</p>
                      <a href="${consent_url}" class="btn btn-outline-primary mt-3 consent">Yes</a>
                      <a href="/donor/stories/" class="btn btn-outline-primary mt-3">No</a>
                      </div>
                    </div>
                  </div>
                    </div>
                
            </div>
            `;
            //score_url = `${url}${score}/
          
            sleep(1000).then(createScore)
        });

        $.ajax({
            type: 'GET',
            url: `${url}${score}/`,
            success: function(response){
                console.log("score added")
            },
            error: function(error){
                console.log("Error occured adding score")
            }
        })
    }

    i = i + 1;
};

$(document).on("click", ".ans", function () {


    $(this).css({ "color": "white" });
    //$(this).css({ "color": "white" });
    //$(this.chk).removeClass('d-none')
    if ($(this).attr('ans') == 'True') {


        $(this).css({ "backgroundColor": "#44b78b" });
        $(this).html('<i class="fas fa-check me-3 chk"></i>' + $(this).html())

        score = parseInt($('#quiz').attr("score"))
        score = score + 100
        $('#quiz').attr("score", score)
        sleep(1000).then(nextQuestion)
        
    } else {
        $(this).css({ "backgroundColor": "red" });
        $(this).html('<i class="fas fa-times me-3"></i>' + $(this).html())
        sleep(2000).then(nextQuestion)
        //createScore()
    }


});


var createScore = function() {
    console.log("create Score called!")
    $(".progress").each(function() {
  
      var value = $(this).attr('data-value');
      var left = $(this).find('.progress-left .progress-bar');
      var right = $(this).find('.progress-right .progress-bar');
      console.log(value)
  
      if (value > 0) {
        if (value <= 50) {
          right.css('transform', 'rotate(' + percentageToDegrees(value) + 'deg)')
        } else {
          right.css('transform', 'rotate(180deg)')
          left.css('transform', 'rotate(' + percentageToDegrees(value - 50) + 'deg)')
        }
      }
  
    })
  
    function percentageToDegrees(percentage) {
  
      return percentage / 100 * 360
  
    }
  
  }

//$();
  

