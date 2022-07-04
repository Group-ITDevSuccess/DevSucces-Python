(function($) {
    $(document).ready(function(){
        var toggle = $( '#close' );
        if ( ! toggle.data( 'visible' ) ) {
            $( '#toclistclose' ).hide();
        }
        toggle.click( function( ) {
   
            if ( $( this ).data( 'visible' ) ) {
                $( this ).data( 'visible', false );
                $( '#toclistclose' ).hide( 'fast' );
                 $( '#close' ).text('show');
            } else {
                $( this ).data( 'visible', true );
                $( '#toclistclose' ).show( 'fast' );
                 $( '#close' ).text('hide');
        

            }
            
        } );

        //  for when open
        var toggle = $( '#open' );
        if ( ! toggle.data( 'visible' ) ) {
            $( '#toclist' ).show();
        }
        toggle.click( function( ) {
   
            if ( $( this ).data( 'visible' ) ) {
                $( this ).data( 'visible', false );
                $( '#toclist' ).show( 'fast' );
                 $( '#open' ).text('hide');
            } else {
                 $( this ).data( 'visible', true );
                $( '#toclist' ).hide( 'fast' );
                 $( '#open' ).text('show');
            }
            
        } );
    
        $('body .gutentoc  a[href*="#"]').on('click', function(e) {
            e.preventDefault()
  
            $('html, body').animate(
              {
                scrollTop: $($(this).attr('href')).offset().top -120,
              },
              500,
              'linear'
            );
          });
          $('body .scroll_id_show  a[href*="#"]').on('click', function() {
            $('html, body').animate(
              {
                scrollTop: $($(this).attr('href')).offset().top -120,
              },
              500,
              'linear'
            );
          })
    
    });
})(jQuery); 