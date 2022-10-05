from mrjob.job import MRJob

from mrjob.step import MRStep



class Types_count(MRJob):
    def steps(self):

        return [

            MRStep(mapper=self.mapper_get_types,

            reducer=self.reducer_types),

            MRStep(reducer=self.reducer_max_count_types)

        ]


    def mapper_get_types(self, _, line):

        (pokemonId,pokemonName,pokemonType1,pokemonType2,HP,Attack,Defense,SpAttack,SpDef,Speed,Generation,Lengendary) = line.split(',')

        if pokemonId != "#":

                yield (pokemonType1, (1, Defense))

                


    def reducer_types(self, key, values):

        totalNumber,totalDefense=0,0

        for value in values:

            totalNumber += value[0]

            totalDefense += int(value[1])

        yield None, (totalDefense/totalNumber, key)


    def reducer_max_count_types(self, _, values):

        yield max(values)


if __name__ == '__main__':

    Types_count.run()
