import csv
import random

# Creates an instance of a team
# Require Day 0 ELO rating for a team

class Team:
	def __init__(self,name, initial_elo):
		self.schedule = []
		self.name = name
		self.elo = initial_elo
		self.wins = 0
		self.losses = 0

	def updateEloRating(self, old_elo, ex_win, win):
		#ELO Rating update on win. 1 is the value of a win, 0 for a loss. ex_win is calculated within Game.playGame
		new_elo = old_elo
		if(win):
			new_elo = new_elo + round(float(32 *(1 - ex_win)))
			return new_elo
		else:
			new_elo = new_elo + round(float(32 *(0 - ex_win)))
			return new_elo


# Creates an instance of a Game
# Required input: Home Team, Away Team (of type Team)

class Game:
	def __init__(self,home_team, away_team):
		self.home_team = home_team
		self.away_team = away_team
		self.winner = None

	def playGame(self):
		print self.home_team.name + " (" + str(self.home_team.elo) + ") is playing " + self.away_team.name + " (" + str(self.away_team.elo) + ")"
		#calculate expectation for home team to win
		expectation_home_win = 1/float((1+(float(10)**((self.away_team.elo - self.home_team.elo)/float(400)))))

		#1-P(Home_win) = P(Away-win)
		expectation_away_win = float(1 - expectation_home_win)

		#Calculate a random number between 0 and 1
		r = random.random()

		if(expectation_home_win > r):
			self.winner = self.home_team.name

			#home team elo update
			self.home_team.elo = self.home_team.updateEloRating(self.home_team.elo, expectation_home_win, True )

			#increment the number of wins for a home team win
			self.home_team.wins = self.home_team.wins + 1

			#away team elo update
			self.away_team.elo = self.away_team.updateEloRating(self.away_team.elo, expectation_away_win, False )
			#increment the number of losses for a away team loss
			self.away_team.losses = self.away_team.losses + 1
		
		else:
			self.winner = self.away_team.name

			#home team elo update
			self.home_team.elo = self.home_team.updateEloRating(self.home_team.elo, expectation_home_win, False )
			#increment the number of losses for a home team loss
			self.home_team.losses = self.home_team.losses + 1

			#away team elo update
			self.away_team.elo = self.home_team.updateEloRating(self.away_team.elo, expectation_away_win, True )

			#increment the number of wins for a away team win
			self.away_team.wins = self.away_team.wins + 1

		
		print self.winner + " won!"
		return [self.winner, self.home_team, self.away_team]

class Season:
	def __init__(self, teams, schedule):
		self.teams = teams
		self.schedule = schedule

	def playSeason(self, teams):
		temp_teams = teams
		for x, game in enumerate(schedule):
			print "Game number: " + str(x+1)
			outcome = game.playGame()

			for t in temp_teams:
				if (outcome[1].name == t.name):
					t.elo = outcome[1].elo
				if (outcome[2].name == t.name):
					t.elo = outcome[2].elo
		print "------------------ FINAL SEASON STANDINGS ------------------"
		for team in teams:
			out = team.name +" finished with record of "+ str(team.wins) + " - " + str(team.losses) + " and elo of: " + str(team.elo)
			print(out)



def BuildTeams():
	file = open("nfl_elo_ratings.csv")
	csvreader = csv.reader(file)
	header = next(csvreader)
	teams = []
	for row in csvreader:
	    name = row[0]
	    elo = int(row[1])
	    teams.append(Team(name, elo))
	return teams

def BuildSchedule(teams):
	file = open("nfl_schedule.csv")
	csvreader = csv.reader(file)
	header = next(csvreader)
	games = []
	for row in csvreader:
	    home = row[0]
	    away = row[1]
	    home_team = None
	    away_team = None
	    for team in teams:
	    	if(team.name == home):
	    		home_team = team
	    	elif(team.name == away):
	    		away_team = team
	    games.append(Game(home_team, away_team))
	return games

teams = BuildTeams()
schedule = BuildSchedule(teams)

season = Season(teams, schedule)
season.playSeason(teams)