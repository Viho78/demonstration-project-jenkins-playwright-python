#-------------sql insert data
# insert booking data
# insert_legacy, query_verify_legacy, expected_df_legacy, query_verify_new_after_sync, expected_df_new
testdata_happy_1 = [('''USE example_hotel_db_legacy
                            INSERT INTO bookings_legacy (booking_id, first_name, last_name, total_price, deposit_paid, check_in_date, check_out_date, additional_needs, uid_room)
                            VALUES ('BOOK0025', 'Anna', 'Kowalska', 300, 1, '2026-02-01', '2026-02-05', 'Breakfast', 101)
                           '''), 

                          ('''USE example_hotel_db_legacy
                            SELECT bl.booking_id, bl.first_name, bl.last_name, r.room_type, r.price_per_night FROM bookings_legacy bl
                            LEFT JOIN rooms r ON r.uid_room = bl.uid_room
                            WHERE bl.booking_id = 'BOOK0025' '''), 

                          {
                            'booking_id': ['BOOK0025'],
                            'first_name': ['John'],
                            'last_name': ['Kowalski'],
                            'room_type': ['Single Deluxe'],
                            'price_per_night': [1000],
                            }  ,
                            
                          ('''USE example_hotel_db_new
                            SELECT bn.booking_id, bn.first_name, bn.last_name, r.room_type, r.price_per_night FROM bookings_new bn
                            LEFT JOIN rooms r ON r.uid_room = bn.uid_room
                            WHERE bn.booking_id = 'BOOK0025' '''),
                            
                            {
                                'booking_id': ['BOOK0025'],
                                'first_name': ['John'],
                                'last_name': ['Kowalski'],
                                'room_type': ['Single Deluxe'],
                                'price_per_night': [1000],
                                }  
                            ]