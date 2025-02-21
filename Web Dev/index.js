
// A SIMPLE STOPWATCH CODE

// 1 = Constructor

function Stopwatch() {

  var startTime, endTime, running, duration = 0;

  this.start = function() {

    if (running)
        throw new Error('The Stopwatch has already started running.');

    running = true;

    startTime = new Date();

  };

  this.stop = function() {

    if (!running)
        throw new Error('The Stopwatch has not been started yet.');

    running = false;

    endTime = new Date();

    const seconds = (endTime.getTime() - startTime.getTime()) / 1000; // to get the miliseconds

    duration += seconds;

  };

  // setting the variables to their initial values

  this.reset = function() {

    startTime = null;

    endTime = null;

    running = false;

    duration = 0;

  };


  // A read only property called "duration"

  Object.defineProperty(this, 'duration', {
    get: function() { 
      return duration; 
    }
  })

}