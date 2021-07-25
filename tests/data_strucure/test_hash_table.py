from data_structures_and_algorithims_.data_structure.linkedlist.linkedlist import Node, LinkedList
from data_structures_and_algorithims_.data_structure.hash_table.hash_table import HashTable
import pytest

def test_add_to_hashtable(hash_table):
    hash_table.add('bmw',2011)
    assert hash_table.map[hash_table.hash('bmw')].head.value[0]=='bmw'

def test_contains():
    hashTable=HashTable(1024)
    hashTable.add('avanti',97)
    hashTable.add('serato',2000)
    hashTable.add('crv','2006')
    assert hashTable.contains('crv')==True    

def test_get(hash_table):
    assert hash_table.get('crv')==2006


def test_collosion_value(hash_table):
    assert hash_table.hash('listen')==157


def test_collision(hash_table):
    assert hash_table.map[hash_table.hash('qusai')].head.value[1] == 24
    assert hash_table.map[hash_table.hash('qusai')].head.next.value[1] == 25










@pytest.fixture
def hash_table():
    hashTable=HashTable(1024)
    hashTable.add('avanti',97)
    hashTable.add('serato',2000)
    hashTable.add('crv',2006)
    hashTable.add('qusai',24)
    hashTable.add('qusai',25)
    hashTable.add('listen', 'Hey man')
    hashTable.add('silente','bs')
    return hashTable