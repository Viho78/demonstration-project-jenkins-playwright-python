#------------------------------------------------------------------
import pytest
import allure
import testdata_DB
import pandas as pd

@allure.suite("Backend SQL Tests - Contact form")
@allure.story("Item 105888")
@allure.label("owner", "JStanczyk")
class Test_ContactFormTests():
    
    #method to compare dataframes if they match - result returned from query with expected result
    def comparison(self, expected_df, data_df) -> bool:
            try:
                #checking if amount of rows is the asme
                if data_df.shape[0] == expected_df[0].shape[0]:
                    #checking for differences (must be the same shape), compare() returns differences, it there are no diff then returns empty
                    if data_df.compare(expected_df[0]).empty:
                        #correct
                        pass
                    else:
                        print('Verification not ok - different values')
                        print("Differences:", 'red')
                        print(data_df.compare(expected_df[0]))
                        return True #incorrect so it can return
                else:
                    print('Verification not ok - different amount of rows')
                    print("Expected rows:")
                    print(expected_df[0])
                    print("Actual rows:")
                    print(data_df)
                    return True #incorrect so it can return
            except:
                print('Unknown error')
                return True #incorrect so it can return
            return False #all correct
    
    #method to run synchronisation procedure and wait for it to finish
    def run_synchronisation(self, get_new_DB_conn) -> None:
        get_new_DB_conn[0].execute(''' EXEC procedure_sync_legacy_to_new; ''') #[0] to get cursor from the fixture
        get_new_DB_conn[1].commit() #[1] to get conn from the fixture

        #some varification if procedure is finished
        #(I'm not faking anything here as this is just demonstration project)

    
    #Create Booking and Sync from legacy to new DB test
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.parametrize("insert_legacy, query_verify_legacy, expected_df_legacy, query_verify_new_after_sync, expected_df_new", 
                            [testdata_DB.testdata_happy_1,],
                            ids=["sync from legacy 1",])
    def test_create_booking(self, get_legacy_DB_conn, get_new_DB_conn, insert_legacy, query_verify_legacy, expected_df_legacy, query_verify_new_after_sync, expected_df_new):
        #inserting legacy data of booking
        get_legacy_DB_conn[0].execute(insert_legacy) #[0] to get cursor from the fixture
        get_legacy_DB_conn[1].commit() #[1] to get conn from the fixture

        #getting legacy inserted data to verify
        get_legacy_DB_conn[0].execute(query_verify_legacy)
        data = get_legacy_DB_conn[0].fetchall()
        data_df = pd.DataFrame(data)

        #verifing that legacy insert is correct
        assert self.comparison(expected_df_legacy, data_df) == False #false means all correct

        #running synchronisation procedure to sync data from legacy to new DB + waiting for it to finish
        self.run_synchronisation(get_new_DB_conn)

        #getting new synced data to verify
        get_new_DB_conn[0].execute(query_verify_new_after_sync)
        data = get_new_DB_conn[0].fetchall()
        data_df = pd.DataFrame(data)

        #verifing that new synced data is correct
        assert self.comparison(expected_df_new, data_df) == False #false means all correct

if __name__ == "__main__":
    pass