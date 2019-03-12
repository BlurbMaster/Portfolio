from Classy import conversion
import pytest

@pytest.mark.conversion_unit_change
def test_conversion_good_1( ):
    alter = conversion.Conversion( )

    answer = alter.unit_change( 1.2482, ( 'KGS', 'KGS' ) )
    assert answer == pytest.approx( 1.2482, 0.0005 )


@pytest.mark.conversion_unit_change
def test_conversion_good_2( ):
    alter = conversion.Conversion( )

    answer = alter.unit_change( 1.25, ( 'KGS', 'LBS' ) )
    assert answer == pytest.approx( 2.755775, 0.000005 )


@pytest.mark.conversion_unit_change
def test_conversion_good_3( ):
    alter = conversion.Conversion( )

    answer = alter.unit_change( 3, ( 'LBS', 'KGS' ) )
    assert answer == pytest.approx( 1.360776, 0.000005 )


@pytest.mark.conversion_unit_change
def test_conversion_good_4( ):
    alter = conversion.Conversion( )

    answer = alter.unit_change( 1.2483, ( 'LBS', 'LBS' ) )
    assert answer == pytest.approx( 1.2483, 0.0005 )


@pytest.mark.conversion_unit_change
def test_conversion_badType_1( ):
    alter = conversion.Conversion( )

    answer = alter.unit_change( 'frog', ( 'KGS', 'KGS' ) )
    assert answer == None


@pytest.mark.conversion_unit_change
def test_conversion_badType_2( ):
    alter = conversion.Conversion( )

    answer = alter.unit_change( 0, ( 'KGS', 'KGS' ) )
    assert answer == None


@pytest.mark.conversion_unit_change
def test_conversion_badType_3( ):
    alter = conversion.Conversion( )

    answer = alter.unit_change( -15, ( 'KGS', 'KGS' ) )
    assert answer == None


@pytest.mark.conversion_unit_change
def test_conversion_badType_4( ):
    alter = conversion.Conversion( )

    with pytest.raises( ValueError ):
        answer = alter.unit_change( 245.5, ( 'LBS', 'Kopecs' ) )


@pytest.mark.conversion_unit_change
def test_conversion_badType_5( ):
    alter = conversion.Conversion( )

    with pytest.raises( ValueError ):
        answer = alter.unit_change( 245.38,  'Kopecs'  )
