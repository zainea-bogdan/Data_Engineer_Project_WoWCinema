 Insert into bronze_wowcinema.wowcinema_data
        (
        log_id                  ,
        username                ,
        first_name              ,
        last_name             ,
        birth_date,
        subscription_plan       ,
        subscription_start_date ,
        iban                    ,
        title_name              ,
        watch_start_time        ,
        watch_end_time          ,
        session_duration_min    ,
        rating_given            ,
        reaction_type           ,
        region_code            
        )
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ;