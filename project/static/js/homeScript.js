window.onload = function () {
    Vue.component('event-item', {
        props: ['event'],
        template: '\
        <div>\
            <p> {{ event.location }}  \
                <button v-on:click="$emit(\'remove\')">Remove</button>\
            </p>\
            <p> {{ event.type }} </p>\
            <p> {{ event.start }} - {{ event.end }} </p>\
        </div>\
        '
    })
      
    var app = new Vue({
	  delimiters: ['[[', ']]'],
	  el: '#app',
	  data: {
        eventList: [
            { id: 0, location: 'Cazuelas', type: 'Restaurant', start: '5:00 pm', end: '6:30 pm' },
            { id: 1, location: 'Newport', type: 'Concert', start: '7:00 pm', end: '11:00 pm' },
            { id: 2, location: 'Dahlia', type: 'Club', start: '12:00 am', end: '2:00 am'},
        ],
        addEventString: '+ Add Event',
      },
      computed: {
        showBottomEventButton: function () {
            return this.eventList.length > 0
        }
      },
      created: function () {

      },
    });
}