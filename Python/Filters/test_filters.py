from Classy import filters
from datetime import datetime
import pytest

# Test bad arguments
def test_wrong_no_args( ):
    sieve = filters.Filter( )
    
    with pytest.raises( TypeError ):
        answer = sieve.decode_field( "test_table", "goodFieldName"  )

# Test various bogus arguments
def test_bad_arg_type_1( ):
    sieve = filters.Filter( )

    with pytest.raises( TypeError ):
        answer = sieve.decode_field( 7, "goodFieldName", '1971-11-11'  )
       
def test_bad_arg_type_2( ):
    sieve = filters.Filter( )

    with pytest.raises( TypeError ):
        answer = sieve.decode_field( "test_table", 7, '1971-11-11'  )
      
def test_bad_arg_type_3( ):
    sieve = filters.Filter( )

    with pytest.raises( TypeError ):
        answer = sieve.decode_field( 7, 7, '1971-11-11'  )

def test_bad_table_name( ):
    sieve = filters.Filter()

    with pytest.raises( IndexError ):
        answer = sieve.decode_field( 'weirdo', 'goodFieldName', '1971-11-11'  )


def test_bad_field_name( ):
    sieve = filters.Filter()

    with pytest.raises( IndexError ):
        answer = sieve.decode_field( 'test_table', 'weirdo', '1971-11-11'  )

def test_unimplemented( ):
    sieve = filters.Filter()

    with pytest.raises( NotImplementedError ):
        answer = sieve.decode_field( 'test_table', 'bogusFieldType', '1971-11-11'  )

@pytest.mark.filter_dateTest
def test_date_null( ):
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'goodFieldName', None  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_date_empty_string( ):
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'goodFieldName', ''  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_date_bad_date_type_1( ):
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'goodFieldName', 7  )
    assert answer == None

#
# Going to be picky here and insist that simple 'date' types and 'datetimes'
# are different things and are not handled together.
#
@pytest.mark.filter_dateTest
def test_date_bad_date_type_2( ):
    sieve = filters.Filter()
    myDateTime = datetime.strptime( '1971-11-11', '%Y-%m-%d' )
    answer = sieve.decode_field( 'test_table', 'goodFieldName', myDateTime  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_datetime_null_date_string():
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'goodFieldName', '0000-00-00'  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_date_bad_date_string():
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'goodFieldName', '1971-14-14'  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_date_good_date_string():
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'goodFieldName', '1971-11-11'  )
    myDateTime = datetime.strptime( '1971-11-11', '%Y-%m-%d' )
    myDate = myDateTime.date()
    assert answer == myDate

@pytest.mark.filter_dateTest
def test_date_good_date_object( ):
    sieve = filters.Filter()
    myDateTime = datetime.strptime( '1971-11-11', '%Y-%m-%d' )
    myDate = myDateTime.date()
    answer = sieve.decode_field( 'test_table', 'goodFieldName', myDate  )
    assert answer == myDate

@pytest.mark.filter_dateTest
def test_dateTime_null( ):
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'dateTimeName', None  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_dateTime_empty_string( ):
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'dateTimeName', ''  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_dateTime_bad_date_type_1( ):
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'dateTimeName', 7  )
    assert answer == None

#
# Going to be picky here and insist that simple 'date' types and 'datetimes'
# are different things and are not handled together.
#
@pytest.mark.filter_dateTest
def test_dateTime_bad_date_type_2( ):
    sieve = filters.Filter()
    myDateTime = datetime.strptime( '1971-11-11', '%Y-%m-%d' )
    myDate = myDateTime.date()
    answer = sieve.decode_field( 'test_table', 'dateTimeName', myDate  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_dateTime_null_date_string():
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'dateTimeName', '0000-00-00 00:00:00'  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_dateTime_bad_date_string():
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'dateTimeName', '1971-14-14 12:12:12'  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_dateTime_bad_time_string():
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'dateTimeName', '1971-11-11 25:12:12'  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_dateTime_good_date_string():
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'dateTimeName', '1971-11-11 12:12:13'  )
    myDateTime = datetime.strptime( '1971-11-11 12:12:13', '%Y-%m-%d %H:%M:%S' )
    assert answer == myDateTime

@pytest.mark.filter_dateTest
def test_dateTime_good_dateTime_object( ):
    sieve = filters.Filter()
    myDateTime = datetime.strptime( '1971-11-11 12:12:13', '%Y-%m-%d %H:%M:%S' )
    answer = sieve.decode_field( 'test_table', 'dateTimeName', myDateTime  )
    assert answer == myDateTime

@pytest.mark.filter_dateTest
def test_deltaTime_good_bytes_object( ):
    from datetime import timedelta

    sieve = filters.Filter()
    myDeltaTime = timedelta( days = 13 )
    answer = sieve.decode_field( 'test_table', 'intervalName', b'13'  )
    assert answer == myDeltaTime

@pytest.mark.filter_dateTest
def test_deltaTime_good_string_object( ):
    from datetime import timedelta

    sieve = filters.Filter()
    myDeltaTime = timedelta( days = 13 )
    answer = sieve.decode_field( 'test_table', 'intervalName', '13'  )
    assert answer == myDeltaTime

@pytest.mark.filter_dateTest
def test_deltaTime_good_int_object( ):
    from datetime import timedelta

    sieve = filters.Filter()
    myDeltaTime = timedelta( days = 13) 
    answer = sieve.decode_field( 'test_table', 'intervalName', 13  )
    assert answer == myDeltaTime

@pytest.mark.filter_dateTest
def test_deltaTime_negative( ):
    from datetime import timedelta

    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'intervalName', -13  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_deltaTime_zero( ):
    from datetime import timedelta

    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'intervalName', '0'  )
    assert answer == None

@pytest.mark.filter_dateTest
def test_deltaTime_bad_string( ):
    from datetime import timedelta

    sieve = filters.Filter()
    with pytest.raises( ValueError ):
        answer = sieve.decode_field( 'test_table', 'intervalName', 'La-la-la!'  )

@pytest.mark.filter_dateTest
def test_deltaTime_Too_Late( ):
    from datetime import timedelta

    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'intervalName', 1611  )
    assert answer == timedelta( days = 1500 )


@pytest.mark.filter_dateTest
def test_deltaTime_good_real_object( ):
    from datetime import timedelta

    sieve = filters.Filter()
    myDeltaTime = timedelta( days = 13 )
    answer = sieve.decode_field( 'test_table', 'intervalName', 13.8  )
    assert answer == myDeltaTime   # Note the truncation

@pytest.mark.filter_dateTest
def test_deltaTime_deltatime_object( ):
    from datetime import timedelta

    sieve = filters.Filter()
    myDeltaTime = timedelta( days = 13  )
    passedDeltaTime = timedelta( days = 13, hours = 4 )  # Note the truncation
    answer = sieve.decode_field( 'test_table',
                                     'intervalName',
                                     passedDeltaTime )
    assert answer == myDeltaTime

#
# Not too many tests for the integer version of  delta times since it calls
# the standard date interval filter routine and that should have all been
# tested above.
#
@pytest.mark.filter_dateTest
def test_date_dayInt_null():
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'intIntervalName', '0'  )
    assert answer == None
        
@pytest.mark.filter_dateTest
def test_date_dayInt_goodInt():
    sieve = filters.Filter()
    answer = sieve.decode_field( 'test_table', 'intIntervalName', 5  )
    assert answer == 5
    assert type( answer ) == int

@pytest.mark.filter_IDTest
def test_app_id_bad_type( ):
    from datetime import timedelta
    sieve = filters.Filter()
    myDeltaTime = timedelta( days = 13 )

    answer = sieve.decode_field( 'test_table', 'idName', myDeltaTime )
    assert answer == None 
   
@pytest.mark.filter_IDTest
def test_app_id_bad_string_1( ):
    sieve = filters.Filter()

    answer = sieve.decode_field( 'test_table', 'idName', '-5' )
    assert answer == None

@pytest.mark.filter_IDTest
def test_app_id_bad_string_2( ):
    sieve = filters.Filter()

    answer = sieve.decode_field( 'test_table', 'idName', '0' )
    assert answer == None

@pytest.mark.filter_IDTest
def test_app_id_bad_string_3( ):
    sieve = filters.Filter()

    answer = sieve.decode_field( 'test_table', 'idName', 'La-la-la!' )
    assert answer == None

@pytest.mark.filter_IDTest
def test_app_id_good_string( ):
    sieve = filters.Filter()

    answer = sieve.decode_field( 'test_table', 'idName', '1234' )
    assert answer == 1234

@pytest.mark.filter_IDTest
def test_app_id_good_int( ):
    sieve = filters.Filter()

    answer = sieve.decode_field( 'test_table', 'idName', 1234 )
    assert answer == 1234

@pytest.mark.filter_IDTest
def test_app_id_bad_int( ):
    sieve = filters.Filter()

    answer = sieve.decode_field( 'test_table', 'idName', -2 )
    assert answer == None

@pytest.mark.filter_IDTest
def test_db_id_bad_type( ):
    from datetime import timedelta
    sieve = filters.Filter()
    myDeltaTime = timedelta( days = 13 )

    with pytest.raises( ValueError ):
        answer = sieve.decode_field( 'test_table', 'DbIdName', myDeltaTime )

@pytest.mark.filter_IDTest
def test_db_id_bad_string_1( ):
    sieve = filters.Filter()

    with pytest.raises( ValueError ):
        answer = sieve.decode_field( 'test_table', 'DbIdName', '-5' )

@pytest.mark.filter_IDTest
def test_db_id_bad_string_2( ):
    sieve = filters.Filter()

    with pytest.raises( ValueError ):
        answer = sieve.decode_field( 'test_table', 'DbIdName', '0' )

@pytest.mark.filter_IDTest
def test_db_id_bad_string_3( ):
    sieve = filters.Filter()

    with pytest.raises( ValueError ):
        answer = sieve.decode_field( 'test_table', 'DbIdName', 'La-la-la!' )

@pytest.mark.filter_IDTest
def test_db_id_good_string( ):
    sieve = filters.Filter()

    answer = sieve.decode_field( 'test_table', 'DbIdName', '1234' )
    assert answer == 1234

@pytest.mark.filter_IDTest
def test_db_id_good_int( ):
    sieve = filters.Filter()

    answer = sieve.decode_field( 'test_table', 'DbIdName', 1234 )
    assert answer == 1234

@pytest.mark.filter_IDTest
def test_db_id_bad_int( ):
    sieve = filters.Filter()

    with pytest.raises( ValueError ):
        answer = sieve.decode_field( 'test_table', 'DbIdName', -4 )

@pytest.mark.filter_stringTest
def test_string_empty():
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'stringName', '' )
    assert answer == None

@pytest.mark.filter_stringTest
def test_string_corrupt_1():
    sieve = filters.Filter( )

    myBadString = chr( 27 ) + chr( 97 )
    answer = sieve.decode_field( 'test_table', 'stringName', myBadString )

    assert type( answer ) == str
    assert answer == 'Corrupt string #1'

@pytest.mark.filter_stringTest
def test_string_corrupt_2():
    sieve = filters.Filter( )

    myBadString = chr( 27 ) + chr( 97 )
    answer = sieve.decode_field( 'test_table', 'stringName', myBadString )

    assert type( answer ) == str
    assert answer == 'Corrupt string #2'

@pytest.mark.filter_stringTest
def test_string_good_string_1( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'stringName', 'goodString' )
    assert type( answer ) == str
    assert answer == 'goodString'

@pytest.mark.filter_stringTest
def test_string_good_string_2( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'stringName', b'goodString' )
    assert type( answer ) == str
    assert answer == 'goodString'

@pytest.mark.filter_stringTest
def test_string_good_string_3( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'stringName', bytearray( b'goodString' ) )
    assert type( answer ) == str
    assert answer == 'goodString'

@pytest.mark.filter_stringTest
# Handle both offical languages!
def test_string_good_string_4( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'stringName', 'accepté' )
    assert type( answer ) == str
    assert answer == 'accepté'

@pytest.mark.filter_stringTest
def test_string_good_string_5( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'stringName', bytes( 'accepté', 'utf-8' ) )
    assert type( answer ) == str
    assert answer == 'accepté'

@pytest.mark.filter_stringTest
def test_string_good_string_6( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'stringName', 42 )
    assert type( answer ) == str
    assert answer == '42'


@pytest.mark.filter_stringTest
def test_string_good_province_1( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field(  'test_table', 'provinceName', 'ON' )

    assert answer == '35'


@pytest.mark.filter_stringTest
def test_string_good_province_2( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field(  'test_table', 'provinceName', 'Newfoundland and Labrador' )

    assert answer == '10'


@pytest.mark.filter_stringTest
def test_string_bad_province_1( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field(  'test_table', 'provinceName', 'Slobovia' )

    assert answer == None


@pytest.mark.filter_stringTest
def test_string_bad_province_2( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field(  'test_table', 'provinceName', None )

    assert answer == None

    
@pytest.mark.filter_booleanTest
def test_boolean_good_False_byte( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'booleanName', b'0' )
    assert answer == False

@pytest.mark.filter_booleanTest
def test_boolean_good_True_byte( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'booleanName', b'1' )
    assert answer == True

@pytest.mark.filter_booleanTest
def test_boolean_bad_byte_1( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'booleanName', b'6' )
    assert answer == None

@pytest.mark.filter_booleanTest
def test_boolean_bad_byte_2( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'booleanName', b'' )
    assert answer == None

@pytest.mark.filter_booleanTest
def test_boolean_bad_type_1( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'booleanName', None )
    assert answer == None

@pytest.mark.filter_booleanTest
def test_boolean_bad_type_2( ):
    sieve = filters.Filter( )
    myDateTime = datetime.strptime( '1971-11-11 12:12:13', '%Y-%m-%d %H:%M:%S' )
    
    with pytest.raises( NotImplementedError ):
        answer = sieve.decode_field( 'test_table', 'booleanName',  myDateTime )

@pytest.mark.filter_booleanTest
def test_boolean_good_True_Int( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'booleanName', 1 )
    assert answer == True

@pytest.mark.filter_booleanTest
def test_boolean_good_False_Int( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'booleanName', 0 )
    assert answer == False

@pytest.mark.filter_booleanTest
def test_boolean_good_True_bool( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'booleanName', True )
    assert answer == True

@pytest.mark.filter_booleanTest
def test_boolean_good_False_bool( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'booleanName', False )
    assert answer == False

@pytest.mark.filter_posRealTest
def test_posReal_goodFloat_1( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'posRealName', 5.5123 )
    assert answer == 5.5123

@pytest.mark.filter_posRealTest
def test_posReal_goodInt( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'posRealName', 8 )
    assert answer == 8.0
    assert type( answer ) == float
    
@pytest.mark.filter_posRealTest
def test_posReal_goodByte( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'posRealName', b'8' )
    assert answer == 8.0
    assert type( answer ) == float
    
@pytest.mark.filter_posRealTest
def test_posReal_goodString( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'posRealName', '8' )
    assert answer == 8.0
    assert type( answer ) == float
    
@pytest.mark.filter_posRealTest
def test_posReal_Negativity( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'posRealName', '-8' )
    assert answer == None
       
@pytest.mark.filter_posRealTest
def test_posReal_BadReal_1( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'posRealName', '8,45' )
    assert answer == None
    
@pytest.mark.filter_posRealTest
def test_posReal_BadReal_2( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'posRealName', 'blahblahblah' )
    assert answer == None
    

@pytest.mark.filter_posRealTest
def test_posReal_BadReal_3( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'posRealName', 0.0 )
    assert answer == None

@pytest.mark.filter_genderTest
def test_gender_goodSex_1( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'genderName', 'Male' )
    assert answer == 'male'


@pytest.mark.filter_genderTest
def test_gender_goodSex_2( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'genderName', 'female' )
    assert answer == 'female'


@pytest.mark.filter_genderTest
def test_gender_goodSex_3( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'genderName', b'male' )
    assert answer == 'male'


@pytest.mark.filter_genderTest
def test_gender_goodSex_4( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'genderName', ' Male  ' )
    assert answer == 'male'


@pytest.mark.filter_genderTest
def test_gender_goodSex_5( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'genderName', ' dAme' )
    assert answer == 'female'


@pytest.mark.filter_genderTest
def test_gender_badSex_1( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'genderName', 'fred' )
    assert answer == None

    
@pytest.mark.filter_genderTest
def test_gender_badSex_2( ):
    sieve = filters.Filter( )

    answer = sieve.decode_field( 'test_table', 'genderName', 1.069 )
    assert answer == None


@pytest.mark.filter_pandasDateTest
def test_pandas_datetime_goodDate_1( ):
    import datetime

    constructor = filters.Pandas_Fix( )

    myDateObject = datetime.datetime( 2011, 1, 1, 2, 2, 2)
    answer = constructor.decode_cell( 'ptest_table', 'datetimeName', myDateObject )

    assert answer == 365

@pytest.mark.filter_pandasDateTest
def test_pandas_datetime_goodDate_2( ):
    import datetime

    constructor = filters.Pandas_Fix( )

    myDateObject = datetime.date( 2011, 1, 2 )
    answer = constructor.decode_cell( 'ptest_table', 'datetimeName', myDateObject )

    assert answer == 366

@pytest.mark.filter_pandasDateTest
def test_pandas_datetime_badDate_1( ):
    import datetime

    constructor = filters.Pandas_Fix( )

    myDateObject = datetime.datetime( 2009, 1, 1, 2, 2, 2)
    answer = constructor.decode_cell( 'ptest_table', 'datetimeName', myDateObject )

    assert answer == None

@pytest.mark.filter_pandasDateTest
def test_pandas_datetime_badDate_2( ):
    import datetime

    constructor = filters.Pandas_Fix( )

    answer = constructor.decode_cell( 'ptest_table', 'datetimeName', 5 )

    assert answer == None

@pytest.mark.filter_pandasDateTest
def test_pandas_datetime_badDate_3( ):
    import datetime

    constructor = filters.Pandas_Fix( )

    answer = constructor.decode_cell( 'ptest_table', 'datetimeName', None )

    assert answer == None
    
@pytest.mark.filter_pandasNaturalNumbersTest
def test_pandas_ZTest_GoodNumber_1( ):
    constructor = filters.Pandas_Fix( )

    answer = constructor.decode_cell( 'ptest_table', 'naturalNumbersName',  None )

    assert answer == 0
   
@pytest.mark.filter_pandasNaturalNumbersTest
def test_pandas_ZTest_GoodNumber_2( ):
    constructor = filters.Pandas_Fix( )

    answer = constructor.decode_cell( 'ptest_table', 'naturalNumbersName',  0 )

    assert answer == 0
   
@pytest.mark.filter_pandasNaturalNumbersTest
def test_pandas_ZTest_GoodNumber_3( ):
    constructor = filters.Pandas_Fix( )

    answer = constructor.decode_cell( 'ptest_table', 'naturalNumbersName',  286 )

    assert answer == 286

#
# We'll actually accept 'float's and retain their mantissas as type conversions
# between different layers of software often hand us such things when given
# integers.
#
@pytest.mark.filter_pandasNaturalNumbersTest
def test_pandas_ZTest_GoodNumber_4( ):
    constructor = filters.Pandas_Fix( )

    answer = constructor.decode_cell( 'ptest_table', 'naturalNumbersName',  4.5 )

    assert answer == 4.5
   
@pytest.mark.filter_pandasNaturalNumbersTest
def test_pandas_ZTest_GoodNumber_5( ):
    constructor = filters.Pandas_Fix( )

    answer = constructor.decode_cell( 'ptest_table', 'naturalNumbersName',  -5 )

    assert answer == 0

    
@pytest.mark.filter_pandasNaturalNumbersTest
def test_pandas_ZTest_BadType( ):
    constructor = filters.Pandas_Fix( )

    with pytest.raises( ValueError ):
        answer = constructor.decode_cell( 'ptest_table', 'naturalNumbersName',  'Fred' )


@pytest.mark.filter_pandasBooleanTest
def test_pandas_boolean_GoodValue_1(  ):
    constructor = filters.Pandas_Fix( )
    answer = constructor.decode_cell( 'ptest_table', 'booleanName',  True )

    assert answer == 1

    
@pytest.mark.filter_pandasBooleanTest
def test_pandas_boolean_GoodValue_2(  ):
    constructor = filters.Pandas_Fix( )
    answer = constructor.decode_cell( 'ptest_table', 'booleanName',  False )

    assert answer == -1

    
@pytest.mark.filter_pandasBooleanTest
def test_pandas_boolean_GoodValue_3(  ):
    constructor = filters.Pandas_Fix( )
    answer = constructor.decode_cell( 'ptest_table', 'booleanName',  0 )

    assert answer == -1

    
@pytest.mark.filter_pandasBooleanTest
def test_pandas_boolean_GoodValue_4(  ):
    constructor = filters.Pandas_Fix( )
    answer = constructor.decode_cell( 'ptest_table', 'booleanName',  1 )

    assert answer == 1
    

@pytest.mark.filter_pandasBooleanTest
def test_pandas_boolean_GoodValue_5(  ):
    constructor = filters.Pandas_Fix( )
    answer = constructor.decode_cell( 'ptest_table', 'booleanName',  88 )

    assert answer == 1

    
@pytest.mark.filter_pandasBooleanTest
def test_pandas_boolean_GoodValue_6(  ):
    constructor = filters.Pandas_Fix( )
    answer = constructor.decode_cell( 'ptest_table', 'booleanName',  -5 )

    assert answer == 1

    
@pytest.mark.filter_pandasBooleanTest
def test_pandas_boolean_BadType( ):
    constructor = filters.Pandas_Fix( )

    with pytest.raises( ValueError ):
        answer = constructor.decode_cell( 'ptest_table', 'booleanName',  'Fred' )

        
@pytest.mark.filter_pandasGenderBender
def test_pandas_GenderBender_GoodSex_1( ):
    import numpy as np;
    import pandas as pd;
    constructor = filters.Pandas_Fix( )

    start = pd.DataFrame( { 'id': [ 1, 2, 3, 4], 'sex': [ 'male', 'female', 'noThankyou', 'male']
        } )

    #
    # Remember that the default result will have columns sorted by column name in
    # alphabetical order.
    #
    expected = pd.DataFrame( { 'female': [ 0, 1, 0, 0], 'male': [ 1, 0, 0, 1], 
                                   'noThankyou':[ 0, 0, 1, 0]
        } )

    #
    # Right now the underlyimg pandas code in the utility that we're testing
    # 'helpfully' compresses everything to int8 so we have to match that.
    #
    expected = expected.astype( np.uint8 )
    
    answer = constructor.decode_cell( 'ptest_table', 'genderName',  start['sex'] )

    from pandas.util.testing import assert_frame_equal

    assert_frame_equal( answer.sort_index( axis=1),
                            expected.sort_index( axis=1),
                            check_names=True )

        
@pytest.mark.filter_pandasGenderBender
def test_pandas_GenderBender_GoodSex_2( ):
    import numpy as np;
    import pandas as pd;
    constructor = filters.Pandas_Fix( )

    start = pd.DataFrame( { 'id': [ 1, 2, 3, 4], 'sex': [ 'male', 'female', None, 'male']
        } )

    #
    # Remember that the default result will have columns sorted by column name in
    # alphabetical order.
    #
    expected = pd.DataFrame( { 'female': [ 0, 1, 0, 0], 'male': [ 1, 0, 0, 1], 
                                   'unspecified':[ 0, 0, 1, 0]
        } )

    #
    # Right now the underlyimg pandas code in the utility that we're testing
    # 'helpfully' compresses everything to int8 so we have to match that.
    #
    expected = expected.astype( np.uint8 )
    
    answer = constructor.decode_cell( 'ptest_table', 'genderName',  start['sex'] )

    from pandas.util.testing import assert_frame_equal

    assert_frame_equal( answer.sort_index( axis=1),
                            expected.sort_index( axis=1),
                            check_names=True )

        
@pytest.mark.filter_pandasGenderBender
def test_pandas_GenderBender_BadArg( ):
    import numpy as np;
    import pandas as pd;
    constructor = filters.Pandas_Fix( )

    with pytest.raises( TypeError ):
        answer = constructor.decode_cell( 'ptest_table', 'genderName',  ['mail', 'other'] )    


def test_pandas_GenderBender_sp_prefix( ):
    import numpy as np;
    import pandas as pd;
    constructor = filters.Pandas_Fix( )

    start = pd.DataFrame( { 'id': [ 1, 2, 3, 4], 'sex': [ 'male', 'female', None, 'male']
        } )

    #
    # Remember that the default result will have columns sorted by column name in
    # alphabetical order.
    #
    expected = pd.DataFrame( { 'sp_female': [ 0, 1, 0, 0], 'sp_male': [ 1, 0, 0, 1], 
                                   'sp_unspecified':[ 0, 0, 1, 0]
        } )

    #
    # Right now the underlyimg pandas code in the utility that we're testing
    # 'helpfully' compresses everything to int8 so we have to match that.
    #
    expected = expected.astype( np.uint8 )
    
    answer = constructor.decode_cell( 'ptest_table', 'sp_genderName',  start['sex'] )

    from pandas.util.testing import assert_frame_equal

    assert_frame_equal( answer.sort_index( axis=1),
                            expected.sort_index( axis=1),
                            check_names=True )
    
