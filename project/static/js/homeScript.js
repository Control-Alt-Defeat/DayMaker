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
                <p class="eventTitle"> {{ event.location }}</p>\
                <p class="eventDetails"> {{ event.type }} </p>\
                <p class="eventDetails"> {{ event.start_formatted }} - {{ event.end_formatted }} </p>\
            </div>\
            <div class="eventColumnRight">\
                <p>\
                    <a :href="\'/planner/edit/\' + parseInt(event.id, 10) + \'/\'" > \
                    <div :id=event.id class="removeEventButton eventDetails">\
                        <a :href="\'/planner/\' + parseInt(event.plan_id,10) + \'/edit/\' + parseInt(event.id, 10) + \'/\'" > \
                        <i class="fa fa-pencil-square-o"></i>\
                        Edit\
                        </a>\
                    </div>\
                    </a>\
                    <a :href="\'/planner/delete/\' + parseInt(event.id, 10) + \'/\'" > \
                    <div :id=event.id class="removeEventButton eventDetails">\
                        <a :href="\'/planner/\' + parseInt(event.plan_id,10) + \'/delete/\' + parseInt(event.id, 10) + \'/\'" > \
                        <i class="fa fa-trash"></i>\
                        Remove\
                        </a>\
                    </div>\
                    </a>\
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
        dateOfPlan: '',
      },
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
    methods : {
        getPlanData: function() {
            fetch("/ajax/get-date-of-plan/").then(response => response.json()).then((json) => {
                this.dateOfPlan = json['dateOfPlan']
            })
        },
        convertEventTimes: function() {

        }
    }
    });

    app.getPlanData();
}
