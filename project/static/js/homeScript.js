window.onload = function () {
    Vue.component('event-item', {
        props: ['event'],
        template: '\
        <div>\
            <div class="eventColumnLeft eventDetails"">\
                <p> {{ event.address }} </p>\
                <p> {{ event.price }} </p>\
            </div>\
            <div class="eventColumnMiddle">\
                <p class="eventTitle"> {{ event.location }}  \
                </p>\
                <p class="eventDetails"> {{ event.type }} </p>\
                <p class="eventDetails"> {{ event.start }} - {{ event.end }} </p>\
            </div>\
            <div class="eventColumnRight">\
                <p>\
                    <button v-on:click="$emit(\'remove\')">Remove</button>\
                </p>\
            </div>\
        </div>\
        '
    })
      
    var app = new Vue({
	  delimiters: ['[[', ']]'],
	  el: '#app',
	  data: {
        eventList: [
            { id: 0, location: 'Cazuelas', type: 'Restaurant', start: '5:00 pm', end: '6:30 pm', address: '123 North High Street', price: '$' },
            { id: 1, location: 'Newport', type: 'Concert', start: '7:00 pm', end: '11:00 pm', address: '2231 North High Street', price: '$' },
            { id: 2, location: 'Dahlia', type: 'Club', start: '12:00 am', end: '2:00 am', address: '3000 North High Street', price: '$$'},
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