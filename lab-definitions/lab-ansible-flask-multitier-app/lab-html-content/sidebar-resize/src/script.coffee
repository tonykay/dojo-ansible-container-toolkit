dragging = false
ghost = null

$doc = $(document)

$(".slider").on "mousedown", (e) ->
	e.preventDefault()
	
	dragging = true
	width = $(".content").width()
	offsetX = $(".content").offset().left
	
	ghost = $("<div/>",
						class: "ghostSlider"
						css: 
							left: $(".properties").offset().left - offsetX
	).appendTo $(".content")

	$(".size").text(parseInt($(".properties").width()) + "px").fadeIn("fast")

	$doc.on "mousemove", (ev) ->
		dragging = true
		ghost.css left: ev.pageX - offsetX
		$(".size").text(parseInt(width - ev.pageX + offsetX) + "px")
		
	$doc.on "mouseup", (ev) ->
		e.preventDefault()
		if dragging
			$doc.off "mousemove mouseup"
			$(".properties").css "flex": "0 0 " + (width - ghost.offset().left + offsetX) + "px"
			ghost.remove();
			dragging = false
			
			$(".size").fadeOut("slow")
			
