window.onload = function () {
    Vue.component('event-item', {
        props: ['event'],
        template: '\
        <div>\
            <div class="eventColumnLeft eventDetails"">\
                <i class="fa fa-car"></i>\
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
                    <button class="removeEventButton eventDetails" v-on:click="$emit(\'remove\')">\
                        <i class="fa fa-trash"></i>\
                        Remove\
                    </button>\
                </p>\
            </div>\
        </div>\
        '
    })
      
    var app = new Vue({
	  delimiters: ['[[', ']]'],
	  el: '#app',
	  data: {
        eventList: event_list,
        addEventString: '+ Add Event',
      },
    //   mounted: function() {
    //     this.getEvents();
    //   },
      computed: {
        showBottomEventButton: function () {
            return this.eventList.length > 0
        }
      },
    //   methods: {
    //     getEvents: function() {
    //         console.log('getEvents() ran')
    //         this.loading = true;
    //         //this.$http.get('/api/event/')
    //         fetch('/api/event/')
    //             .then((response) => {
    //               console.log('received data in getEvents()')
    //               console.log(response)
    //               this.eventList = response.data;
    //               this.loading = false;
    //             })
    //             .catch((err) => {
    //              this.loading = false;
    //              console.log(err);
    //             })
    //     },
    //   }
    });
}