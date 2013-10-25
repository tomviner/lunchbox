(function ( $ ) {
    "use strict";
    var sparqler = new SPARQL.Service("http://linkedgeodata.org/sparql");
    sparqler.setOutput("json");
    sparqler.setMethod("GET");
    sparqler.addDefaultGraph("http://linkedgeodata.org");
    sparqler.setPrefix("lgdo", "http://linkedgeodata.org/ontology/"); 
    sparqler.setPrefix("fn", "http://www.w3.org/2005/xpath-functions#");
    sparqler.setPrefix("geo", "http://www.w3.org/2003/01/geo/wgs84_pos#");

    $(function(){
        var sparql_template = Handlebars.compile($('#rando-rest-query').html()),
            resturant_template = Handlebars.compile($('#restaurant-template').html()),
            resturant_placeholder = $('#restuarants-placeholder')

        sparqler.query(
            sparql_template({
                "date": new Date().toDateString()
            }),
            {
                "success": function(data){
                    resturant_placeholder.html(
                        resturant_template({
                            "restaurants" : data["results"]["bindings"]
                        })
                    );
                    console.log(                        resturant_template({
                            "restaurants" : data["results"]["bindings"]
                        }));
                },
                "failure": function(){
                    debugger;
                }
            }
        )

        resturant_placeholder.on("click", "button.vote", function(event){
            var button = $(event.target),
                restaurant = button.parent("a").attr("href");
            $.ajax({
                type: "POST",
                url: "/vote/",
                data: {"restaurant": restaurant},
                success: function(data){
                    if (data.status == "add") {
                        button.attr("disabled", "disabled")
                    } else {
                        li_elem.css( {"background-color": "#fff"} )
                        button.removeAttr("disabled")
                    }
                    li_elem.find('.votes').html(data.votes);
                }
            });
        })

    });
}( jQuery ));